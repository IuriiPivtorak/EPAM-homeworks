#!/usr/bin/env python3.6


from itertools import islice
import operator


def get_data():
    """Function that just returns our data.
    """
    return [{'name': 'Alexey', 'rate': 2, 'course': 'Python'},
            {'name': 'Yana', 'rate': 5, 'course': 'Python'},
            {'name': 'Sergei', 'rate': 3, 'course': 'Python'},
            {'name': 'Katerina', 'rate': 5, 'course': 'Python'},
            {'name': 'Alexey', 'rate': 10, 'course': 'Java'},
            {'name': 'Evgeny', 'rate': 6, 'course': 'Java'},
            {'name': 'Artem', 'rate': 5, 'course': 'Java'},
            {'name': 'Kirill', 'rate': 6, 'course': 'Java'},
            {'name': 'Egor', 'rate': 1, 'course': 'Scala'}]


def get_courses(data):
    """Creates set of courses in data.

    :param data: our data.
    :returns: set.
    """
    return {item['course'] for item in data}


def get_top_students(data, course):
    """Gets top 3 students for each course.

    :param data: our data.
    :param course: name of course.
    :returns: list.
    """
    # sorting each student for each course by rate,
    # then with islice getting only top 3 students
    return islice(sorted([(item['name'], item['rate'])
                          for item in data if item['course'] == course],
                         key=operator.itemgetter(1), reverse=True), 0, 3)


def get_students_top_table(course):
    """Creates table of top 3 students for each course.

    :param course: course name.
    :returns: table.
    """
    return 'COURSE {}\n'.format(course) + \
           '\n'.join('{:10} ---> {:4}'.format(*name)
                     for name in get_top_students(get_data(), course))


def get_table():
    """Printing our table.
    """
    print('\n'.join(get_students_top_table(course)
                    for course in get_courses(get_data())))


if __name__ == '__main__':
    get_table()
