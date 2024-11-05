t = \
{
  "CardSubwayStatsNew": {
    "list_total_count": 618,
    "RESULT": {
      "CODE": "INFO-000",
      "MESSAGE": "정상 처리되었습니다"
    },
    "row": [
      {
        "USE_YMD": "20240830",
        "SBWY_ROUT_LN_NM": "1호선",
        "SBWY_STNS_NM": "서울역",
        "GTON_TNOPE": 63216,
        "GTOFF_TNOPE": 60119,
        "REG_YMD": "20240902"
      },
      {
        "USE_YMD": "20240830",
        "SBWY_ROUT_LN_NM": "1호선",
        "SBWY_STNS_NM": "시청",
        "GTON_TNOPE": 31658,
        "GTOFF_TNOPE": 32336,
        "REG_YMD": "20240902"
      },
      {
        "USE_YMD": "20240830",
        "SBWY_ROUT_LN_NM": "1호선",
        "SBWY_STNS_NM": "종각",
        "GTON_TNOPE": 43781,
        "GTOFF_TNOPE": 43496,
        "REG_YMD": "20240902"
      },
      {
        "USE_YMD": "20240830",
        "SBWY_ROUT_LN_NM": "1호선",
        "SBWY_STNS_NM": "종로3가",
        "GTON_TNOPE": 27463,
        "GTOFF_TNOPE": 25024,
        "REG_YMD": "20240902"
      },
      {
        "USE_YMD": "20240830",
        "SBWY_ROUT_LN_NM": "1호선",
        "SBWY_STNS_NM": "종로5가",
        "GTON_TNOPE": 26598,
        "GTOFF_TNOPE": 25874,
        "REG_YMD": "20240902"
      }
    ]
  }
}

print(type(t))
print(t["CardSubwayStatsNew"]['row'][3]["SBWY_STNS_NM"])
print(type(t["CardSubwayStatsNew"]['row'][3]["SBWY_STNS_NM"]))
# print result below
# <class 'dict'>
# 종로3가
# <class 'str'>