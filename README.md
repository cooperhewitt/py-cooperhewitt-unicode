# py-cooperhewitt-unicode

Tools for working with Unicode data

## Example

### cooperhewitt.unicode.names

    import cooperhewitt.unicode.names as names
    import sys

    input = sys.argv[1:]
    input = " ".join(input)

    input = input.decode('utf-8')

    ref = names.lookup()

    for char in input:
        name = ref.name(char)
        print "%s is %s" % (char, name)

## Scripts

### ucd-name

Display the Unicode name for one or more characters

	/usr/local/bin/ucd-name ☃
	SNOWMAN

	/usr/local/bin/ucd-name ☈ 
	THUNDERSTORM

	/usr/local/bin/ucd-name Mr ☃!
	LATIN CAPITAL LETTER M
	LATIN SMALL LETTER R
	SPACE
	SNOWMAN
	EXCLAMATION MARK

### build-ucd-lookup

Fetch UCD data and export as a JSON dictionary mapping hex value to Unicode name

	/usr/local/bin/build-ucd-lookup > data/lookup.json

## See also

* http://unicode.org/Public/UCD/latest/ucd/
