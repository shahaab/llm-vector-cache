import argparse
from engine.store import VectorStore

store = VectorStore(max_size=1000)

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="command")

add_cmd = subparsers.add_parser("add")
add_cmd.add_argument("--id", required=True)
add_cmd.add_argument("--vector", nargs='+', type=float, required=True)

search_cmd = subparsers.add_parser("search")
search_cmd.add_argument("--vector", nargs='+', type=float, required=True)
search_cmd.add_argument("--topk", type=int, default=5)

args = parser.parse_args()

if args.command == "add":
    store.add(args.id, args.vector)
    print(f"✅ Added {args.id}")
elif args.command == "search":
    results = store.search(args.vector, args.topk)
    for id, score in results:
        print(f"{id}: {score:.4f}")
