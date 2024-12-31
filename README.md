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
    <li><a href='#rus-comment-class'>Comment</a></li>
    <li><a href='#rus-friend-class'>Friend</a></li>
    <li><a href='#rus-team-class'>Team</a></li>
    <li><a href='#rus-team-member-class'>TeamMember</a></li>
</ul>

<section id='rus-user-class'>
    <h3><b>User</b> class</h3>
    <section>
        <dl>
            <dt>class <b>User</b>(id: int, autoparse: bool=True)</dt>
            <dd>
                <p>Класс, собирающий информацию о пользователе и представляющий его.</p>
                <dl id='rus-user-id'>
                    <dt>User.id</dt>
                    <dd>
                        Уникальный айди пользователя.
                    </dd>
                </dl>
                <dl id='rus-user-autoparse'>
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
            </dd>
        </dl>
    </section>
    <section id='rus-user-methods'>
        <h4><b>Методы</b></h4>
        <section id='rus-user-get-bookmarks'>
            <dl>
                <dt>User.get_bookmarks(sort_by: str='name', sort_type: str='desc', status: Status=statuses.ALL, site: Site=sites.MANGALIB, as_json: bool=False, count: int=None) -> list[Bookmark]|dict </dt>
                <dd>
                    <p>Возвращает закладки пользователя.</p>
                    <dl id='rus-user-get-bookmarks-params'>
                        <dt>Параметры:</dt>
                        <dd>
                            <dl id='rus-user-get-bookmarks-sort-by-values'>
                                <dt>sort_by :</dt>
                                <dd>
                                    <ul>
                                        <li>'name' - cортировка по английскому алфавиту.</li>
                                        <li>'rus_name' - cортировка по русскому алфавиту.</li>
                                        <li>'created_at' - cортировка по дате добавления.</li>
                                        <li>'updated_at' - cортировка по дате чтения.</li>
                                        <li>'last_chapter_at' - cортировка по дате обновления глав.</li>
                                    </ul>
                                </dd>
                            </dl>
                            <dl id='rus-user-get-bookmarks-sort-type-values'>
                                <dt>sort_type :</dt>
                                <dd>
                                    <ul>
                                        <li>'desc' - сортировка по убыванию.</li>
                                        <li>'asc' - сортировка по возрастанию.</li>
                                    </ul>
                                </dd>
                            </dl>
                            <dl id='rus-user-get-bookmarks-status-values'>
                                <dt>status :</dt>
                                <dd>
                                    <p>То, какого статуса будут закладки, которые будут парситься(Читаю, Смотрю, Прочитано и т.д.). По умолчанию стоит ВСЕ. Импорт с помощью <i><b>from mangalib_parser import statuses</i></b></p>
                                </dd>
                            </dl>
                            <dl id='rus-user-get-bookmarks-site-values'>
                                <dt>site :</dt>
                                <dd>
                                    <p>То, с какого сайта будут закладки, которые будут парситься(Мангалиб, Ранобелиб, Анимелиб и т.д.). По умолчанию стоит Мангалиб. Импорт с помощью <i><b>from mangalib_parser import sites</i></b></p>
                                </dd>
                            </dl>
                            <dl id='rus-user-get-bookmarks-as-json-values'>
                                <dt>as_json :</dt>
                                <dd>
                                    <p>От этого параметра зависит, будет ли полученный словарь с закладками конвертирвоаться в лист из класса Bookmark.</p>
                                </dd>
                            </dl>
                            <dl id='rus-user-get-bookmarks-count-values'>
                                <dt>count :</dt>
                                <dd>
                                    <p>Сколько закладок возвратит функция.</p>
                                </dd>
                            </dl>
                        </dd>
                    </dl>
                </dd>
            </dl>
        </section>
        <section id='rus-user-get-comments'>
            <dl>
                <dt>User.get_comments(sort_by: str='id', sort_type: str='desc', as_json: bool=False, count: int=None) -> list[Comment]|dict</dt>
                <dd>
                    <p>Возвращает комментарии пользователя.</p>
                    <dl id='rus-user-get-comments-params'>
                        <dt>Параметры:</dt>
                        <dd>
                            <dl id='rus-user-get-comments-sort-by-values'>
                                <dt>sort_by :</dt>
                                <dd>
                                    <ul>
                                        <li>'id' - сортировка по времени.</li>
                                        <li>'votes' - сортировка по рейтингу.</li>
                                    </ul>
                                </dd>
                            </dl>
                            <dl id='rus-user-get-comments-sort-type-values'>
                                <dt>sort_type :</dt>
                                <dd>
                                    <ul>
                                        <li>'desc' - сортировка по убыванию.</li>
                                        <li>'asc' - сортировка по возрастанию.</li>
                                    </ul>
                                </dd>
                            </dl>
                            <dl id='rus-user-get-comments-as-json-values'>
                                <dt>as_json :</dt>
                                <dd>
                                    <p>От этого параметра зависит, будет ли полученный словарь с комментариями конвертирвоаться в лист из класса Comment.</p>
                                </dd>
                            </dl>
                            <dl id='rus-user-get-comments-count-values'>
                                <dt>count :</dt>
                                <dd>
                                    <p>Сколько закладок возвратит функция.</p>
                                </dd>
                            </dl>
                        </dd>
                    </dl>
                </dd>
            </dl>
        </section>
        <section id='rus-user-get-friends'>
            <dl>
                <dt>User.get_friends(as_json: bool=False, count: int=None) -> list[Friend]|dict</dt>
                <dd>
                    <p>Возвращает друзей пользователя.</p>
                    <dl id='rus-user-get-friends-params'>
                        <dt>Параметры:</dt>
                        <dd>
                            <dl id='rus-user-get-friends-as-json-values'>
                                <dt>as_json :</dt>
                                <dd>
                                    <p>От этого параметра зависит, будет ли полученный словарь с друзьями конвертирвоаться в лист из класса Friend.</p>
                                </dd>
                            </dl>
                            <dl id='rus-user-get-friends-count-values'>
                                <dt>count :</dt>
                                <dd>
                                    <p>Сколько друзей возвратит функция.</p>
                                </dd>
                            </dl>
                        </dd>
                    </dl>
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
            <p>Закладка тайтла.</p>
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
                <dd>Статус чтения тайтла(Читаю, Прочитано и т.д.). Импорт с помощью  <i><b>from mangalib_parser import statuses</i></b></dd>
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
                <dd>Сайт, на котором опубликован данный тайтл. Можно импоритровать с помощью <i><b>from mangalib_parser import sites</i></b></dd>
            </dl>
            <dl id='rus-bookmark-model'>
                <dt>Bookmark.model</dt>
                <dd>Модель, тип или же класс объекта. Можно импоритровать с помощью <i><b>from mangalib_parser import models</i></b></dd>
            </dl>
        </dd>
    </dl>
    </section>
</section>

<section id='rus-comment-class'>
    <h3><b>Comment</b> class</h3>
    <section>
        <dl>
            <dt>class <b>Comment</b>(chapter: int|None, page, page: int, status: statuses.Status, created_at: datetime, updated_at: datetime, name: str, rus_name: str, slug_url: str, site: sites.Site, model: str, urL: str)</dt>
            <dd>
                <p>Комментарий пользователя.</p>
                <dl id='rus-comment-comment'>
                    <dt>Comment.comment</dt>
                    <dd>Текст комментария с html тегами.</dd>
                </dl>
                <dl id='rus-comment-id'>
                    <dt>Comment.id</dt>
                    <dd>Уникальный айди комментария.</dd>
                </dl>
                <dl id='rus-comment-created-at'>
                    <dt>Comment.created_at</dt>
                    <dd>Дата и время написания комментария.</dd>
                </dl>
                <dl id='rus-comment-user-id'>
                    <dt>Comment.user_id</dt>
                    <dd>Уникальный айди пользователя, написавшего комментарий.</dd>
                </dl>
                <dl id='rus-comment-votes'>
                    <dt>Comment.votes</dt>
                    <dd>Список с лайками и дизлайками комментария, хранится в виде листа, где на первом месте количество дизлайков, а на втором количество лайков.</dd>
                </dl>
                <dl id='rus-comment-relation-type'>
                    <dt>Comment.relation_type</dt>
                    <dd>Модель, тип или же класс объекта, к котороиу был написан комментарий. Можно импоритровать с помощью <i><b>from mangalib_parser import models</i></b></dd>
                </dl>
                <dl id='rus-comment-slug-url'>
                    <dt>Comment.slug_url</dt>
                    <dd>Уникальный слаг тайтла/коллекции/отзыва с помощью которого создаются ссылки связанные с ним. Также используется для быстрого нахождения тайтла/коллекции/отзыва в базе данных.</dd>
                </dl>
                <dl id='rus-comment-site'>
                    <dt>Comment.site</dt>
                    <dd>Сайт, на котором опубликован данный тайтл. Можно импоритровать с помощью <i><b>from mangalib_parser import sites</i></b></dd>
                </dl>
                <dl id='rus-comment-url'>
                    <dt>Comment.url</dt>
                    <dd>Полная ссылка на комментарий.</dd>
                </dl>
            </dd>
        </dl>
    </section>
</section>

<section id='rus-friend-class'>
    <h3><b>Friend</b> class</h3>
    <section>
    <dl>
        <dt>class <b>Friend</b>(user_id: int, **kwargs)</dt>
        <dd>
            <p>Друг пользователя.</p>
            <dl id='rus-friend-user-id'>
                <dt>Friend.user_id</dt>
                <dd>Уникальный айди пользователя на профиль друга.</dd>
            </dl>
            <dl id='rus-friend-comment'>
                <dt>Friend.comment</dt>
                <dd>Как друг записан у пользователя.</dd>
            </dl>
            <dl id='rus-friend-created-at'>
                <dt>Friend.created_at</dt>
                <dd>Дата и время добавления друга.</dd>
            </dl>
            <dl id='rus-friend-status'>
                <dt>Friend.status</dt>
                <dd>Статус отношений с другом(Заявка отправлена, Заявка принята и т.д.)</dd>
            </dl>
        </dd>
    </dl>
    </section>
</section>

<section id='rus-team-class'>
    <h3><b>Team</b> class</h3>
    <section>
    <dl>
        <dt>class <b>Team</b>(id: int, slug_url: str, autparse: bool=True)</dt>
        <dd>
            <p>Команда переводчиков.</p>
            <dl id='rus-team-id'>
                <dt>Team.user_id</dt>
                <dd>Уникальный айди команды.</dd>
            </dl>
            <dl id='rus-team-slug-url'>
                <dt>Team.slug_url</dt>
                <dd>Уникальный слаг команды.</dd>
            </dl>
            <dl id='rus-team-autoparse'>
                <dt>Team.autoparse</dt>
                <dd>Параметр, от которого зависит, будет ли парситься больше информации о команде при инициализации нового объекта класса. По умолчанию True.</dd>
            </dl>
            <dl id='rus-team-url'>
                <dt>Team.url</dt>
                <dd>Ссылка на профиль команды.</dd>
            </dl>
            <dl id='rus-team-name'>
                <dt>Team.name</dt>
                <dd>Название команды.</dd>
            </dl>
            <dl id='rus-team-discord'>
                <dt>Team.discord</dt>
                <dd>Ссылка на Discord команды.</dd>
            </dl>
            <dl id='rus-team-vk'>
                <dt>Team.vk</dt>
                <dd>Ссылка на ВКонтакте команды.</dd>
            </dl>
            <dl id='rus-team-website'>
                <dt>Team.website</dt>
                <dd>Ссылка на вебсайт команды.</dd>
            </dl>
        </dd>
    </dl>
    </section>
</section>

<section id='rus-team-member-class'>
    <h3><b>TeamMember</b> class</h3>
    <section>
    <dl>
        <dt>class <b>TeamMember</b>(user_id: int, **kwargs)</dt>
        <dd>
            <p>Участник команды переводчиков.</p>
            <dl id='rus-team-member-user-id'>
                <dt>TeamMember.user_id</dt>
                <dd>Уникальный айди пользователя, являющегося участником команды.</dd>
            </dl>
            <dl id='rus-team-member-roles'>
                <dt>TeamMember.roles</dt>
                <dd>Роли, принадлежащие участнику команды.</dd>
            </dl>
            <dl id='rus-team-member-permissions'>
                <dt>TeamMember.permissions</dt>
                <dd>Права, принадлежащие участнику команды.</dd>
            </dl>
            <dl id='rus-team-member-team-id'>
                <dt>TeamMember.team_id</dt>
                <dd>Айди команды, участником которой является пользователь.</dd>
            </dl>
        </dd>
    </dl>
    </section>
</section>