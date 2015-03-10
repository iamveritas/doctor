/*
* Змінює закінчення об’єкта в залежності від кількісного номера
* Наприклад, 1 об’єкт але 5 об’єктів
* */
function number_of_objects(number, obj_1, obj_2, obj_3)
{
    if (number == '1')
        return obj_1;
    if (number == '2' ||
        number == '3' ||
        number == '4')
        return obj_2;
    if (number == '5' ||
        number == '6' ||
        number == '7' ||
        number == '8' ||
        number == '9')
        return obj_3;
    if (number[number.length-1] == '1' &&
        number[number.length-2] != '1')
        return obj_1;
    if ((number[number.length-1] == '2' ||
        number[number.length-1] == '3' ||
        number[number.length-1] == '4') &&
        number[number.length-2] != '1')
        return obj_2;
    else
        return obj_3;
}

/*
* Видаляє пробільні символи на початку і вкінці рядка
* */
function trim(str)
{
    return str.replace(/^\s+|\s+$/g, '');
}

number_doctors = trim(document.getElementById('number_of_doctors').innerHTML);
number_of_doctors_text = number_of_objects(number_doctors, 'лікар', 'лікаря', 'лікарів');
document.getElementById('number_of_doctors_text').innerHTML = number_of_doctors_text;

number_reviews = trim(document.getElementById('number_of_reviews').innerHTML);
number_of_reviews_text = number_of_objects(number_reviews, 'відгук', 'відгуки', 'відгуків');
document.getElementById('number_of_reviews_text').innerHTML = number_of_reviews_text;