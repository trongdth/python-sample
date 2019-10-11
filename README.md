# python-sample

## Sample 1: news feed

- Use https://newsapi.org/ as data source.
- Command:
    + Get newest news in your country and save to cache
    ```shell
        python main.py -c update
    ```
    + Search news in cache based on author
    ```shell
        python main.py -c search -a adam
    ```
    + Search news in cache based on source
    ```shell
        python main.py -c search -s bbc
    ```

## Sample 2: user management

- Use users.json and orgs.json as data source.
- Search org name returns all users inside this org in human readable.
- Command:
    ```shell
        python main.py -n apple 
    ```

## Home work:

### Sample 1:
- Cache your data to database like sqlite or mysql instead of json.

### Sample 2:
- Capture user input instead of using argparse.
