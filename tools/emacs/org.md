# org mode

## todo management

### capture

	C-c c select

### sub task

We can manage our task in a hierarchical manner by adding `[/]`
after the task name[^1]. If we need to recursively manage the tasks
we need to add the following property to the task:

	:PROPERTIES:
	:COOKIE_DATA: recursive
	:END:

[^1]: http://qiita.com/akisute3@github/items/821ea2b1e20f575c222f


## Agenda

### Add/remove an org file to the agenda file list

1. configuration

	(setq org-agenda-files (list "~/worklog/gtd.org"
                             "~/worklog/schedule.org"))

2. command

	C-c [ : Add the current file to the front
	C-c ] : Remove from agenda file list
