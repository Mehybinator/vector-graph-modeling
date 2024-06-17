<!-- PROJECT LOGO -->
<h1 align="center">IR System - Vector Graph Modeling</h1>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#built-with">Built With</a></li>
    <li><a href="#prerequisites">Prerequisites</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

## Built With

* ![Colorama][Colorama]
* ![Python][Python]
* ![Pandas][Pandas]
* ![Nltk][Nltk]

<!-- GETTING STARTED -->
## Prerequisites

Initialize a New Python Environment:
```sh
python -m pip venv env
```

Activate The Env by Running:
```sh
env\Scripts\activate
```

And Install Requirements:
```sh
python -m pip install -r requirement.txt
```

<!-- USAGE EXAMPLES -->
## Usage

Run The Code With The Following Command:
```sh
python main.py
```

Alternatively If The Env Is Not Active:
```sh
.\env\Scripts\python main.py
```

In The Prompt You Can Search For A Document, Leading To A Result Much Like How A Google Search Would Look Using The Vector Graph Modeling Technique.

You Can Also Use The data_to_matrix.py File To Create A Matrix Of The Words In Your Documents:
```sh
python data_to_matrix.py
```

This Will Generate A matrix.csv File That main.py Can Use To Search.

This Also Means That You Can Use Your Own Documents File In The Style Of data.csv An Use Your Own Dataset.

<!-- CONTACT -->
## Contact
Mehran Arkak - mehran.arkak@protonmail.com

[Colorama]: https://img.shields.io/badge/Colorama--Learn-EEEEEE?style=for-the-badge&logo=python
[Python]: https://img.shields.io/badge/Python-EEEEEE?style=for-the-badge&logo=python
[Pandas]: https://img.shields.io/badge/Pandas-EEEEEE?style=for-the-badge&logo=python
[Nltk]: https://img.shields.io/badge/Nltk-EEEEEE?style=for-the-badge&logo=python
