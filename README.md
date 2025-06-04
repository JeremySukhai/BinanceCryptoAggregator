<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
***
***
***
*** To avoid retyping too much info. Do a search and replace for the following:
*** github_username, repo_name, twitter_handle, email, project_title, project_description
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/Jeremy1599/Binance-Flask-App">
    <img src="https://public.bnbstatic.com/image/cms/blog/20200707/631c823b-886e-4e46-b12f-29e5fdc0882e.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Binance API Flask App</h3>

  <p align="center">
    Flask app that uses Binance API to get historical and current data of various crypto currencies as well as Account information such as holdings and buy/sell history.
    Data is stored and also displayed through real time charts.
    <br />
    <br />
    <br />
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#updates">Updates</a></li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->

## About The Project

A simple project using Python, Flask and Binance API to aggregate crypto data and output it onto charts of various
sorts.

### Updates

    * SQLAlchemy basic components added to flaskApp.py

### Built With

* [TA-Lib](https://ta-lib.org/)
* [TA-Lib Python wrapper](https://mrjbq7.github.io/ta-lib/install.html)
* [Flask](https://flask.palletsprojects.com/en/2.0.x/)

<!-- GETTING STARTED -->

## Getting Started

To get a local copy up and running follow these steps.

### Requirements

  <a href="https://ta-lib.org/hdr_dw.html">TA-Lib</a>

  <a href="https://mrjbq7.github.io/ta-lib/install.html">Python wrapper for TA-Lib</a>

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/JeremySukhai/BinanceCryptoAggregator.git
   ```
2. Install TA-Lib


4. Install packages to pip from correct requirements file

    * Linux
    ```sh
    pip install -r requirements-linux.txt
    ```

5. Enter API key and password in Config.py
   

7. Run Flask Application
   ```sh
   export FLASK_APP=flaskApp.py
   export FLASK_ENV=development
   flask run
   ```

   If you want to run the Flask app for the entire LAN, do:
   ```sh
   flask run --host:0.0.0.0
   ```
   Connect using IPV4:5000

<!-- ROADMAP -->

## Roadmap

* Store historical BTCBUSD data periodically to /dataset/
* Create function to find gap between aggregate data and current time so it can be filled
* Create modular form of /dataset/ that allows for any token pair to be chosen for aggregation by user.
* Chart that allows for selecting different token pairs (via dropdown-menu most likely)
* Optimize HTML5 & CSS with a framework for better UI & compatibility
* Implement a bscscan query api to get crypto funds from a variety of networks instead of just binance

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->

## Contact

Project Link: [https://github.com/Jeremy1599/Binance-Flask-App](https://github.com/Jeremy1599/Binance-Flask-App)






<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo.svg?style=for-the-badge

[contributors-url]: https://github.com/github_username/repo/graphs/contributors

[forks-shield]: https://img.shields.io/github/forks/github_username/repo.svg?style=for-the-badge

[forks-url]: https://github.com/github_username/repo/network/members

[stars-shield]: https://img.shields.io/github/stars/github_username/repo.svg?style=for-the-badge

[stars-url]: https://github.com/github_username/repo/stargazers

[issues-shield]: https://img.shields.io/github/issues/github_username/repo.svg?style=for-the-badge

[issues-url]: https://github.com/github_username/repo/issues

[license-shield]: https://img.shields.io/github/license/github_username/repo.svg?style=for-the-badge

[license-url]: https://github.com/github_username/repo/blob/master/LICENSE.txt

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555

[linkedin-url]: https://linkedin.com/in/github_username
