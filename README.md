# download-content

## Usage

```
<a href"http://download-content.herokuapp.com
    ?content=123,123
    &&mimetype=application/csv
    &&filename=test.csv">Download CSV</a>
```

## Why
Because somtimes HTML5 isn't supported in Safari and you can't even
download blobs from javascript.
https://github.com/eligrey/FileSaver.js/#safari-61
