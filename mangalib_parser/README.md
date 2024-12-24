<h1 align='center'>👨‍💻️Author: <a href='https://github.com/kooflixy'>kooflixy</a></h1>

<p>Mangalib_parser - библиотека для парсинга различных структур сайта https://mangalib.me/ и дочерних ему</p>


<h1>RUS</h1>

<h2>Навигация</h2>
<ul>
    <li><a href='#rus-classes-title'>Классы</a></li>
</ul>

<h2 id='rus-classes-title'>Классы</h1>
<ul>
    <li><a href='#rus-user-class'>User</a></li>
    <li><a href='#rus-bookmark-class'>Bookmark</a></li>
</ul>

<section id='rus-user-class'>
    <h3><b>User</b> class</h3>
    <section>
        <dl>
            <dt>class <b>User</b>(id: int, autoparse: bool=True)</dt>
            <dd>Класс, собирающий информацию о пользователе и представляющий его.</dd>
        </dl>
        <section>
            <dl id='rus-user-id'>
                <dt>User.id</dt>
                <dd>
                    Уникальный айди пользователя.
                </dd>
            </dl>
            <dl id='rus-user-id'>
                <dt>User.autoparse</dt>
                <dd>
                    Параметр, от которого зависит, будет ли парситься больше информации о пользователя при инициализации нового объекта класса. По умолчанию True.
                </dd>
            </dl>
            <dl id='rus-user-url'>
                <dt>User.url</dt>
                <dd>
                    Ссылка на профиль пользователя.
                </dd>
            </dl>
            <dl id='rus-user-username'>
                <dt>User.username</dt>
                <dd>
                    Имя в профиле пользователя.
                </dd>
            </dl>
            <dl id='rus-user-about'>
                <dt>User.about</dt>
                <dd>
                    Описание в профиле пользователя.
                </dd>
            </dl>
            <dl id='rus-user-last-online-at'>
                <dt>User.last_online_at</dt>
                <dd>
                    Дата и время, когда пользователь был в сети в последний раз.
                </dd>
            </dl>
            <dl id='rus-user-created-at'>
                <dt>User.created_at</dt>
                <dd>
                    Дата и время создания профиля пользователя.
                </dd>
            </dl>
            <dl id='rus-user-level'>
                <dt>User.level</dt>
                <dd>
                    Информация об уровне пользователя.
                </dd>
            </dl>
            <dl id='rus-user-teams'>
                <dt>User.teams</dt>
                <dd>
                    Список с командами переводчиков, в которых состоит пользователь.
                </dd>
            </dl>
        </section>
    </section>
    <section id='rus-user-methods'>
        <h4><b>Методы</b></h4>
        <section id='rus-user-get-bookmarks'>
            <dl>
                <dt>User.get_bookmarks(sort_by: str='name', sort_type: str='desc', status: Status=statuses.ALL, site: Site=sites.MANGALIB, as_json: bool=False, count: int=None) -> list[Bookmark]|dict </dt>
                <dd>
                    pass
                </dd>
            </dl>
        </section>
        <section id='rus-user-get-comments'>
            <dl>v
                <dt>User.get_comments(sort_by: str='id', sort_type: str='desc', as_json: bool=False, count: int=None) -> list[Comment]|dict</dt>
                <dd>
                    pass
                </dd>
            </dl>
        </section>
    </section>
</section>

<section id='rus-bookmark-class'>
    <h3><b>Bookmark</b> class</h3>
    <section>
    <dl>
        <dt>class <b>Bookmark</b>(chapter: int|None, page, page: int, status: statuses.Status, created_at: datetime, updated_at: datetime, name: str, rus_name: str, slug_url: str, site: sites.Site, model: str, urL: str)</dt>
        <dd>
        Закладка тайтла.
        </dd>
        <section>
            <dl id='rus-bookmark-chapter'>
                <dt>Bookmark.chapter</dt>
                <dd>Глава, на которой остановился пользователь при чтении.</dd>
            </dl>
            <dl id='rus-bookmark-page'>
                <dt>Bookmark.page</dt>
                <dd>Страница, на которой остановился пользователь при чтении.</dd>
            </dl>
            <dl id='rus-bookmark-status'>
                <dt>Bookmark.status</dt>
                <dd>Статус чтения тайтла(Читаю, Прочитано и т.д.). Импорт с помощью  <i><b>from mangalib_parser.data import statuses</i></b></dd>
            </dl>
            <dl id='rus-bookmark-created-at'>
                <dt>Bookmark.created_at</dt>
                <dd>Дата и время добавления тайтла в закладки.</dd>
            </dl>
            <dl id='rus-bookmark-updated-at'>
                <dt>Bookmark.updated_at</dt>
                <dd>Дата и время последней поставленной закладки тайтла.</dd>
            </dl>
            <dl id='rus-bookmark-name'>
                <dt>Bookmark.name</dt>
                <dd>Оригинальное название тайтла.</dd>
            </dl>
            <dl id='rus-bookmark-rus-name'>
                <dt>Bookmark.rus_name</dt>
                <dd>Название тайтла на русском языке.</dd>
            </dl>
            <dl id='rus-bookmark-slug-url'>
                <dt>Bookmark.slug_url</dt>
                <dd>Уникальный слаг тайтла с помощью которого создаются ссылки связанные с ним. Также используется для быстрого нахождения тайтла в базе данных.</dd>
            </dl>
            <dl id='rus-bookmark-site'>
                <dt>Bookmark.site</dt>
                <dd>Сайт, на котором опубликован данный тайтл. Можно импоритровать с помощью <i><b>from mangalib_parser.data import sites</i></b></dd>
            </dl>
            <dl id='rus-bookmark-model'>
                <dt>Bookmark.model</dt>
                <dd>Модель, тип или же класс объекта. Можно импоритровать с помощью <i><b>from mangalib_parser.data import models</i></b></dd>
            </dl>
        </section>
    </dl>
    </section>
    <section id='rus-bookmark-methods'>
        <h4><b>Методы</b></h4>
        <dl>
        Методов пока что нихферштейн
        </dl>
    </section>
</section>