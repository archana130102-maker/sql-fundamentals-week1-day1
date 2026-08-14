# W6D4: Combining Vanna + Superset for Executive Reporting

## Objective

Convert natural language questions into SQL and validate the SQL before execution.

## Database

SQLite database: sales.db

Tables:
- Customers
- Orders
- Employees
- Sales

## Vanna Training

Five natural language to SQL examples were created.

## Testing

Ten natural language queries were tested and their SQL was manually verified.

## Security

SQL validation was added to allow SELECT queries and block dangerous commands.

## CIA Endpoint

POST /cia/sql-analyst

The endpoint accepts a natural language question and returns validated SQL.

## Evidence

- Database connection screenshot
- 5 Q&A training screenshot
- 10 query testing screenshot
- SQL validation screenshot
- CIA endpoint screenshot