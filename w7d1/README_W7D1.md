# W7D1: CIA Data Analyst Mode — CSV Upload + PandasAI Queries

## Dataset
Indian Startup Funding Dataset

- Rows: 3044
- Columns: 10

## Work Completed

1. Loaded the Indian startup funding CSV using Pandas.
2. Installed PandasAI 3.0.0.
3. Created a PandasAI SmartDataframe.
4. Implemented 10 natural-language queries.
5. Added try-except error handling for failed queries.
6. Compared PandasAI with manual Pandas for 3 questions.
7. Saved query results to w7d1_query_results.csv.

## Manual Pandas Comparison

| Question | Result |
|---|---|
| How many startups are in the dataset? | 3044 |
| Which city has the most startups? | Bangalore |
| Which investment type appears most often? | Private Equity |

## Error Handling

The configured API key was available but did not have LLM credits. PandasAI queries therefore failed with an LLM credit error.

The errors were handled using try-except so the program continued running without crashing.

## Files

- w7d1_pandasai.py
- w7d1_query_results.csv
- pandasai.log
- README_W7D1.md

## Conclusion

PandasAI enables natural-language data analysis using an LLM. Manual Pandas provides a reliable fallback when the AI service is unavailable.
