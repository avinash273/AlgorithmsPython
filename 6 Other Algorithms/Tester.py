class Solution:
    def compareVersion (version1: str, version2: str) -> int:
        versions1 = [int(v) for v in version1.split(".")]
        versions2 = [int(v) for v in version2.split(".")]
        for i in range(max(len(versions1),len(versions2))):
            v1 = versions1[i] if i < len(versions1) else 0
            v2 = versions2[i] if i < len(versions2) else 0
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
        return 0

version1 = "7.5.2.4"
version2 = "7.5.3"

print(Solution.compareVersion(version1, version2))