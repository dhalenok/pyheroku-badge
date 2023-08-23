[![SWUbanner](https://raw.githubusercontent.com/vshymanskyy/StandWithUkraine/main/banner-direct-single.svg)](https://github.com/vshymanskyy/StandWithUkraine/blob/main/docs/README.md)

# pyheroku-badge

The simplest way to include a Heroku badge in your README file.

> The idea was blatantly stolen from the [heroku-badge](https://github.com/pussinboots/heroku-badge) project.

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## Usage

Markdown:

```markdown
![Heroku](https://pyheroku-badge.fly.dev/?app=<HEROKU_APP_NAME>&path=<ROUTE>&style=<STYLE>)
```

reStructuredText:

```rst
.. image:: https://pyheroku-badge.fly.dev/?app=<HEROKU_APP_NAME>&path=<ROUTE>&style=<STYLE>
   :target: https://<HEROKU_APP_NAME>.herokuapp.com
   :alt: Heroku
```

Textile:

```textile
!https://pyheroku-badge.fly.dev/?app=<HEROKU_APP_NAME>&path=<ROUTE>&style=<STYLE>!:https://<HEROKU_APP_NAME>.herokuapp.com
```

## Available Styles

| `flat` (Default)                                                                   | `flat-square`                                                                                  | `plastic`                                                                                  |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| ![Heroku](https://github.com/DenisOH/pyheroku-badge/blob/master/public/img/deployed.svg)  | ![Heroku](https://github.com/DenisOH/pyheroku-badge/blob/master/public/img/deployed-flat-square.svg)  | ![Heroku](https://github.com/DenisOH/pyheroku-badge/blob/master/public/img/deployed-plastic.svg)  |
| ![Heroku](https://github.com/DenisOH/pyheroku-badge/blob/master/public/img/failed.svg)    | ![Heroku](https://github.com/DenisOH/pyheroku-badge/blob/master/public/img/failed-flat-square.svg)    | ![Heroku](https://github.com/DenisOH/pyheroku-badge/blob/master/public/img/failed-plastic.svg)    |
| ![Heroku](https://github.com/DenisOH/pyheroku-badge/blob/master/public/img/not-found.svg) | ![Heroku](https://github.com/DenisOH/pyheroku-badge/blob/master/public/img/not-found-flat-square.svg) | ![Heroku](https://github.com/DenisOH/pyheroku-badge/blob/master/public/img/not-found-plastic.svg) |
| ![Heroku](https://github.com/DenisOH/pyheroku-badge/blob/master/public/img/timeout.svg)   | ![Heroku](https://github.com/DenisOH/pyheroku-badge/blob/master/public/img/timeout-flat-square.svg)   | ![Heroku](https://github.com/DenisOH/pyheroku-badge/blob/master/public/img/timeout-plastic.svg)   |

## FAQ

- Heroku badge shows `timeout`

Most likely your app is using free dynos and goes to sleep after 30 minutes of inactivity. If the app is sleeping, it takes roughly 15 seconds to get a response from the application. However, GitHub has a hard timeout for badges which is roughly 4 seconds.  

While [pyheroku-badge](https://github.com/DenisOH/pyheroku-badge/) can work with any Heroku application, it has to return the badge in less than 4 seconds for GitHub to render it. If your app doesn't return a response for HTTP GET request fast enough, you will see the `timeout` badge.

The only solution would be to upgrade your app to the hobby plan.

## License

```
WWWWWW||WWWWWW
 W W W||W W W
      ||
    ( OO )__________
     /  |           \
    /o o|    MIT     \
    \___/||_||__||_|| *
         || ||  || ||
        _||_|| _||_||
       (__|__|(__|__|
```

Code and documentation are available according to the MIT License (see [LICENSE](LICENSE)).
