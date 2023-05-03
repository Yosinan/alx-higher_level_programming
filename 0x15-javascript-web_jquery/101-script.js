// to add new items
$('div#add_item').click(function () {
	$('ul.my_list').append('<li>Item</li>');
});

// to remove items
$('div#remove_item').click(function () {
	$('ul.my_list li:last-child').remove();
});

// to clear list
$('div#clear_list').click(function () {
	$('ul.my_list').empty();
});
