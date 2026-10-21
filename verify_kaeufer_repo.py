#!/usr/bin/env python3
"""Anhang-F-Proof fürs Band 3: QR-Referenz + URL im Vault-F + im live Repo (L-Mode-Prüfung wie Band 2)"""
import subprocess, base64
f = open('/home/pi/ki-os/vault/10-Projekte/KI-Buch-Pflegende/F-Werkzeug-Quelle.md', encoding='utf-8').read()
assert 'das-ki-buch-pflegende-vorlagen' in f, 'URL fehlt im Vault-F'
assert 'build-media/qr-band3.png' in f, 'QR-Referenz fehlt'
assert 'Platzhalter' not in f, 'Platzhalter-Rest im Vault-F'
from PIL import Image
im = Image.open('/home/pi/ki-os/vault/10-Projekte/KI-Buch-Pflegende/illustrationen/qr-band3.png')
assert im.mode == 'L', f'QR-Mode: {im.mode}'
print('Vault-F: URL ✓ QR ✓ kein Platzhalter ✓, QR-Mode L ✓')

kauf = subprocess.run(['gh', 'api', 'repos/robotfreak/das-ki-buch-pflegende-vorlagen/contents/anhaenge/Anhang-F-Werkzeug-Quelle.md', '-H', 'Accept: application/vnd.github.raw'], capture_output=True, text=True).stdout
assert 'das-ki-buch-pflegende-vorlagen' in kauf, 'URL fehlt im Repo-F'
assert 'illustrationen/qr-band3.png' in kauf, 'QR-Referenz fehlt im Repo-F'
print('Repo-F live: URL ✓ QR-Referenz ✓')

out = subprocess.run(['gh', 'api', 'repos/robotfreak/das-ki-buch-pflegende-vorlagen/contents/anhaenge/illustrationen/qr-band3.png', '-H', 'Accept: application/vnd.github.raw'], capture_output=True)
open('/tmp/qr-live-band3.png', 'wb').write(out.stdout)
im2 = Image.open('/tmp/qr-live-band3.png')
print('Live-QR-Mode:', im2.mode, im2.size)
dec = subprocess.run(['zbarimg', '--quiet', '/tmp/qr-live-band3.png'], capture_output=True, text=True).stdout.strip()
print('Live-QR dekodiert:', dec)
assert 'das-ki-buch-pflegende-vorlagen' in dec
print('ALLE BEWEISE OK')
