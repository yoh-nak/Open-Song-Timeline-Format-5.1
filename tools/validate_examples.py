#!/usr/bin/env python3
"""Optional structural inspection of locally supplied OSTF examples.

Selects JSON Schema by exact document discriminators, checks JSON shape and
selected OSTFP inventories/digests/pins. It does not certify full semantic
conformance, DSP, host/plugin execution, authorization or interoperability.
Comp-map/output equivalence, candidate suppression, exclusive output selection,
ownership, reference scopes and all source-range rules remain host obligations.

This revised reference tool was not executed for the 5.1 written release.
Developers may choose to run it with the optional jsonschema>=4 dependency.
"""
from __future__ import annotations

import hashlib
import sys
import zipfile
from pathlib import Path

try:
    from jsonschema import Draft202012Validator
except ImportError as exc:
    raise SystemExit('Install jsonschema: python -m pip install jsonschema') from exc

import ostfp

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / 'schema'
LEGACY = ROOT / 'adopted-4.3' / 'schema'


def strict_json(raw: bytes, source: str):
    return ostfp.parse_json(raw, source)


def load_schemas():
    table = {
        'score:5.1.0': SCHEMAS / 'ostf-5.1.0.schema.json',
        'score:5.0.0': SCHEMAS / 'ostf-5.0.0.schema.json',
        'score:4.3.0': LEGACY / 'ostf-4.3.0.schema.json',
        'production:0.4.0': SCHEMAS / 'ostf-production-session-0.4.schema.json',
        'production:0.3.0': SCHEMAS / 'ostf-production-session-0.3.schema.json',
        'production:0.2.0': LEGACY / 'ostf-production-session-0.2.schema.json',
        'distributed:0.4': SCHEMAS / 'ostf-distributed-session-0.4.schema.json',
        'distributed:0.3': SCHEMAS / 'ostf-distributed-session-0.3.schema.json',
        'distributed:0.2': LEGACY / 'ostf-distributed-session-0.2.schema.json',
        'manifest:1.1.0': SCHEMAS / 'ostf-package-manifest-1.1.schema.json',
        'manifest:1.0.0': SCHEMAS / 'ostf-package-manifest-1.0.schema.json',
        'plugin:1.1.0': SCHEMAS / 'ostf-plugin-context-1.1.schema.json',
        'plugin:1.0.0': SCHEMAS / 'ostf-plugin-context-1.0.schema.json',
    }
    validators = {}
    for name, path in table.items():
        schema = strict_json(path.read_bytes(), str(path))
        Draft202012Validator.check_schema(schema)
        validators[name] = Draft202012Validator(schema,
                                              format_checker=Draft202012Validator.FORMAT_CHECKER)
    return validators


def schema_key(payload):
    """Return a versioned family key, or None for unrecognized supplemental JSON."""
    if not isinstance(payload, dict):
        return None
    if payload.get('format') == 'OSTF':
        return 'score:' + str(payload.get('version'))
    if payload.get('profile') == 'OSTF-Production-Session':
        return 'production:' + str(payload.get('profileVersion'))
    profile = payload.get('profile')
    if isinstance(profile, str) and profile.startswith('OSTF-Distributed-Session-'):
        return 'distributed:' + profile.removeprefix('OSTF-Distributed-Session-')
    if payload.get('packageFormat') == 'OSTFP':
        return 'manifest:' + str(payload.get('packageVersion'))
    if payload.get('protocol') == 'OSTF-Plugin-Context':
        return 'plugin:' + str(payload.get('protocolVersion'))
    return None


def check(validators, key, payload, source):
    if key not in validators:
        raise ValueError(f'{source}: unsupported exact family/version {key!r}')
    errs = sorted(validators[key].iter_errors(payload),
                  key=lambda e: list(map(str, e.absolute_path)))
    if errs:
        err = errs[0]
        where = '/'.join(map(str, err.absolute_path))
        raise ValueError(f'{source}: {key}: {where}: {err.message}')


def validate_package(path: Path, validators):
    ostfp.validate(path)
    with zipfile.ZipFile(path) as z:
        manifest = strict_json(z.read('manifest.json'), str(path) + '/manifest.json')
        check(validators, 'manifest:' + manifest['packageVersion'], manifest, str(path))
        score_raw = z.read(manifest['score']['path'])
        score = strict_json(score_raw, str(path) + '/score')
        check(validators, 'score:' + manifest['score']['version'], score, str(path))
        if hashlib.sha256(score_raw).hexdigest() != manifest['score']['sha256']:
            raise ValueError(f'{path}: Score SHA mismatch')
        if score.get('format') != 'OSTF' or score.get('version') != manifest['score']['version']:
            raise ValueError(f'{path}: manifest Score version mismatch')
        for descriptor in manifest['documents']:
            raw = z.read(descriptor['path'])
            if hashlib.sha256(raw).hexdigest() != descriptor['sha256']:
                raise ValueError(f'{path}: document SHA mismatch: {descriptor["id"]}')
            obj = strict_json(raw, str(path) + '/' + descriptor['path'])
            role = descriptor['role']
            if role == 'productionSession':
                key = 'production:' + descriptor['version']
            elif role == 'distributedSession':
                key = 'distributed:' + descriptor['version']
            else:
                # Opaque supplement/metadata JSON is byte-preserved. A foreign
                # document is never reclassified as a Distributed Session.
                continue
            check(validators, key, obj, str(path) + '/' + descriptor['path'])
        for asset in manifest['assets']:
            raw = z.read(asset['path'])
            if len(raw) != asset['sizeBytes'] or hashlib.sha256(raw).hexdigest() != asset['sha256']:
                raise ValueError(f'{path}: asset byte length or SHA mismatch: {asset["id"]}')


def main():
    validators = load_schemas()
    counts = {'score': 0, 'production': 0, 'distributed': 0,
              'plugin': 0, 'manifest': 0, 'ostfp': 0, 'opaqueJson': 0}
    examples = ROOT / 'examples'
    for path in sorted(examples.rglob('*')):
        if not path.is_file():
            continue
        if path.suffix == '.ostfp':
            validate_package(path, validators)
            counts['ostfp'] += 1
        elif path.suffix in ('.ostf', '.json'):
            parsed = strict_json(path.read_bytes(), str(path))
            key = schema_key(parsed)
            if path.suffix == '.ostf' and (key is None or not key.startswith('score:')):
                raise ValueError(f'{path}: .ostf requires the OSTF Score discriminator')
            if key is None:
                counts['opaqueJson'] += 1
                continue
            check(validators, key, parsed, str(path))
            counts[key.split(':', 1)[0]] += 1
    print('Selected structural/container checks completed:', counts)
    print('Opaque supplemental JSON is checked for JSON syntax only.')
    print('Comp semantics and host behavior require separate implementation checks; '
          'no runtime/interoperability/security certification is asserted.')


if __name__ == '__main__':
    try:
        main()
    except (OSError, ValueError, TypeError, KeyError, zipfile.BadZipFile, ostfp.PackageError) as exc:
        print('ERROR:', exc, file=sys.stderr)
        raise SystemExit(1)
