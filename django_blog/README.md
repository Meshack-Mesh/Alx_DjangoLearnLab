Blog Post Management (CRUD)
---------------------------
Endpoints:
- /posts/            -> list all posts
- /posts/new/        -> create new post (login required)
- /posts/<pk>/       -> view post detail
- /posts/<pk>/edit/  -> edit post (author only)
- /posts/<pk>/delete/-> delete post (author only)

Permissions:
- Create: authenticated users only.
- Update/Delete: only the post's author (UserPassesTestMixin).
- List/Detail: public.

Notes:
- Author is automatically attached in PostCreateView.form_valid().
- Always include {% csrf_token %} in templates.
- Configure LOGIN_URL and redirect settings in settings.py.
