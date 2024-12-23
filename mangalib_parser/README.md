<h1 align='center'>👨‍💻️Author: <a href='https://github.com/kooflixy'>kooflixy</a></h1>

<p>Mangalib_parser - библиотека для парсинга различных структур сайта https://mangalib.me/ и дочерних ему</p>


<h1>RUS</h1>

<h2>Навигация</h2>
<ul>
    <li><a href='#rus-classes-title'>Классы</a></li>
</ul>

<h2 id='rus-classes-title'>Классы</h1>
<ul>
    <li><a href='#rus-bookmark-class'>Bookmark</a></li>
</ul>
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
                <dd>Модель, тип или же класс объекта.</dd>
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