# Website Endpoint Discover

<p align="center">
  <img src="assets/folder.ico" />
</p>

The "Endpoint Discover" project is a Python script designed to help security researchers and penetration testers discover and identify endpoints of a target website. By utilizing a wordlist of potential endpoint names, the script systematically sends HTTP requests to the target website, attempting to access each endpoint. If a response is received from the target server, the script identifies the discovered endpoint and provides relevant information, such as the HTTP status code and response time.
<br><br>
The script takes advantage of the "requests" library to make HTTP requests and the "colorama" library to enhance the output with colored messages. It provides a straightforward command-line interface to specify the target website URL and the wordlist containing potential endpoint names.
<br><br>
This project can be particularly useful for security testing, bug bounty hunting, or any scenario where identifying hidden or undocumented endpoints is critical to assessing a web application's security posture.

## Usage
1. Install the required dependencies:

    Before using the script, ensure that you have the required dependencies installed by running the following command:
    ```commandline
    pip install requests
    ```
2. Running the script:

    Use the following command to run the script:
    ```commandline
    python3 directory_crawler.py -u <target_url> -w <wordlist>
    ```
    - Replace `<target_url>` with the URL of the target website you want to scan for endpoints `(e.g., http://example.com/)`.

    - Replace `<wordlist>` with the path to a valid wordlist file `(e.g., wordlist.txt)` containing potential endpoint names. Each line in the wordlist file should contain a single endpoint name.
  
**Note:** If you want to see only the successes, since you used `sys.stderr` to write the `x` and `.` characters, invoke the script and redirect `stderr` to `/dev/null` so that only files you found are displayed on the console
```commandline
python3 directory_crawler.py -u <target_url> -w <wordlist> 2> /dev/null
```

## Screenshot
![](https://github.com/SaherMuhamed/website-discover-endpoints/blob/master/screenshots/Screenshot_2024-06-16_2.png)

## Important Note:

Please ensure that you have proper authorization to scan and test the target website. Unauthorized scanning of websites or systems is illegal and unethical. Always obtain explicit permission from the website owner before performing any security assessments.
<br><br>
For legal and responsible use of this script, it is recommended to target websites you own or have explicit permission to test for security vulnerabilities

### Updates
- `v1.1.0 - 16/6/2024`:
  1. adding threads functionality so the script can run much more faster and efficiency
  2. control the number of thread using `-t` or `--thread` option `(default=7)`
