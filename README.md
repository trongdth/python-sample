# python-sample

## Sample 1: news feed

- Use https://newsapi.org/ as data source.
- Command:
    + Get newest news in your country and save to cache
    ```python
        python main.py -c update
    ```
    + Search news in cache based on author
    ```python
        python main.py -c search -a adam
    ```
    + Search news in cache based on source
    ```python
        python main.py -c search -s bbc
    ```

## Sample 2: user management

- Use users.json and orgs.json as data source.


## Home work:

### Sample 1:
- Cache your data to database like sqlite or mysql instead of json.

### Sample 2:
- Capture user input instead of using argparse.
