$(function () {

    //Test code
    var footerImages = [{
        title: 'Academy Raider',
        src: 'img/cards/Academy Raider.full.jpg'
    },{
        title: 'Academy Raider',
        src: 'img/cards/Academy Raider.full.jpg'
    },{
        title: 'Academy Raider',
        src: 'img/cards/Academy Raider.full.jpg'
    },{
        title: 'Academy Raider',
        src: 'img/cards/Academy Raider.full.jpg'
    },{
        title: 'Academy Raider',
        src: 'img/cards/Academy Raider.full.jpg'
    },{
        title: 'Academy Raider',
        src: 'img/cards/Academy Raider.full.jpg'
    },{
        title: 'Academy Raider',
        src: 'img/cards/Academy Raider.full.jpg'
    }];

    displayFooterImages(footerImages);
});

function displayFooterImages(cards) {
    var $footerImages = $('#footer-images');
    
    cards.forEach(card => {
        var $cardImg = $('#footer-img-template').clone();
        $cardImg.removeClass('hidden');
        $cardImg.removeAttr('id');
        $cardImg.css('top', (20 + Math.random() * 30) + 'px');
        $cardImg.attr('title', card.title);
        $cardImg.attr('src', card.src);

        $footerImages.append($cardImg);
    });
}