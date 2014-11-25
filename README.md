# py-cooperhewitt-unicode

This is a work in progress and almost certainly has bugs, still.

## Example

	./scripts/build-ucd-lookup.py > data/lookup.json

	./scripts/lookup-ucd-name.py data/lookup.json ☃
	☃ is SNOWMAN

	./scripts/lookup-ucd-name.py data/lookup.json ☈ 
	☈ is THUNDERSTORM

	./scripts/lookup-ucd-name.py data/lookup.json ஔ
	ஔ  is TAMIL LETTER AU

## See also

* http://unicode.org/Public/UCD/latest/ucd/
