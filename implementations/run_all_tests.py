#!/usr/bin/env python3
"""
implementations/ 아래 모든 test_*.py를 한 번에 찾아서 돌린다.
각 폴더가 독립된 모듈 네임스페이스를 쓰므로, 매번 sys.path를 그 폴더로 바꿔서
격리 실행한다. 파일 이름은 트랙마다 다를 수 있다(알고리즘 트랙은
test_solution.py, 프로젝트 트랙은 도구 이름을 따름 — 예: test_catalog_search.py).
"""
import importlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def find_test_files():
    return sorted(ROOT.rglob("test_*.py"))


def run_one(test_file: Path) -> bool:
    test_dir = test_file.parent
    mod_name = test_file.stem
    sys.path.insert(0, str(test_dir))
    try:
        for name in list(sys.modules):
            if name == mod_name or (test_dir / f"{name}.py").exists():
                sys.modules.pop(name, None)
        test_mod = importlib.import_module(mod_name)
        test_mod.run_all()
        return True
    except Exception as e:  # noqa: BLE001 - 요약 리포트용으로 전부 잡아서 계속 진행
        print(f"FAIL {test_file.relative_to(ROOT)}: {e}")
        return False
    finally:
        sys.path.remove(str(test_dir))


if __name__ == "__main__":
    test_files = find_test_files()
    results = {}
    for f in test_files:
        rel = f.relative_to(ROOT)
        print(f"=== {rel} ===")
        results[str(rel)] = run_one(f)
        print()

    passed = sum(results.values())
    total = len(results)
    print(f"요약: {passed}/{total}개 테스트 파일 전체 통과")
    if passed != total:
        sys.exit(1)
