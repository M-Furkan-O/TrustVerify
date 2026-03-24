import argparse
from crypto_utils import generate_keys
from manifest_utils import create_manifest, check_integrity

parser = argparse.ArgumentParser(description="TrustVerify CLI Tool")


parser.add_argument("--init", help="Manifest oluştur", metavar="DIR")
parser.add_argument("--check", action="store_true")
parser.add_argument("--genkeys", action="store_true")

args = parser.parse_args()

if args.init:
    create_manifest(args.init)

elif args.check:
    check_integrity()

elif args.genkeys:
    generate_keys()

else:
    print("Komut giriniz (--help)")