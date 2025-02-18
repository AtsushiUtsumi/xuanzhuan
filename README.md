## 辞書型で管理
ファイル内部で使うクラス名から、importに必要な文字列(Javaなら「import package ...」みたいな)  
[TODO](document/TODO.md)

## PostgreSQLでのカラム情報取得クエリ
```
SELECT
	t.table_name,
	c.column_name,
	c.data_type,
	c.is_nullable,
	(tc.constraint_type = 'PRIMARY KEY') AS is_key
FROM
	(SELECT * FROM information_schema.TABLES WHERE table_schema = 'public' AND table_type = 'BASE TABLE') t
LEFT JOIN
	(SELECT * FROM information_schema.COLUMNS WHERE table_schema = 'public') c
ON
	t.table_name = c.table_name
LEFT JOIN INFORMATION_SCHEMA.TABLE_CONSTRAINTS tc
ON
	tc.table_catalog = t.table_catalog
	AND tc.table_schema = t.table_schema
	AND tc.table_name = t.table_name
ORDER BY
	t.table_name,
	c.ordinal_position;
```
