<!-- ABOUT THE PROJECT -->
## About The Project

[![Vidnet][product-screenshot]](http://192.3.251.114:8000)

Курс [Highload Architect](https://otus.ru/lessons/highloadarchitect/). Базовый скелет социальной сети, который будет развиваться в дальнейших ДЗ. 


### Built With

* [Python](https://www.python.org)
* [Django](https://www.djangoproject.com)
* [Bootstrap](https://getbootstrap.com)
* [MySQL](https://www.mysql.com)

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/avidyakov/vidnet.git
   ```
2. Copy env
   ```sh
   .env.temp > .env
   ```
3. Start services
   ```sh
   docker compose up --build -d
   ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

### Project link

http://192.3.251.114:8000

### Pages

1. **/auth/reg/** Регистрация
3. **/auth/login/** Логин
5. **/auth/logout/** Логаут
7. **/user/user_id/** Страница пользователя
8. **/user/user_id/update/** Настроки
9. **/user/user_id/subscribers/** Подписчики
10. **/user/user_id/subscriptions/** Подписки

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- LICENSE -->
## License

Distributed under the MIT License.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Alex Vidyakov - [@vidyakov](https://t.me/vidyakov) - alex.vidyakov@yandex.ru

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[product-screenshot]: images/screenshot.png
