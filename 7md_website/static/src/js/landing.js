odoo.define(
    '7md_website.landing', function (require) {
        'use strict';
        console.log("ss")
        // let myCarousel = document.querySelectorAll('#featureContainer .carousel .carousel-item');
        // myCarousel.forEach((el) => {
        //     const minPerSlide = 4
        //     let next = el.nextElementSibling
        //     for (var i = 1; i < minPerSlide; i++) {
        //         if (!next) {
        //             // wrap carousel by using first child
        //             next = myCarousel[0]
        //         }
        //         let cloneChild = next.cloneNode(true)
        //         el.appendChild(cloneChild.children[0])
        //         next = next.nextElementSibling
        //     }
        // })

        // let bestSellerCarousel = document.querySelectorAll('#bestSellerCarousel .carousel .carousel-item');
        // bestSellerCarousel.forEach((el) => {
        //     const minPerSlide = 4
        //     let next = el.nextElementSibling
        //     for (var i = 1; i < minPerSlide; i++) {
        //         if (!next) {
        //             // wrap carousel by using first child
        //             next = bestSellerCarousel[0]
        //         }
        //         let cloneChild = next.cloneNode(true)
        //         el.appendChild(cloneChild.children[0])
        //         next = next.nextElementSibling
        //     }
        // })

        // Jquery multi slider
        // var multiItemSlider = (function () {
        //     return function (selector, config) {
        //         var
        //             _mainElement = document.querySelector(selector), // основный элемент блока
        //             _sliderWrapper = _mainElement.querySelector('.slider__wrapper'), // wrapper for .slider-item
        //             _sliderItems = _mainElement.querySelectorAll('.slider__item'), // elements (.slider-item)
        //             _sliderControls = _mainElement.querySelectorAll('.slider__control'), //  controls
        //             _sliderControlLeft = _mainElement.querySelector('.slider__control_left'), // button "LEFT"
        //             _sliderControlRight = _mainElement.querySelector('.slider__control_right'), // button "RIGHT"
        //             _wrapperWidth = parseFloat(getComputedStyle(_sliderWrapper).width), // wrapper width
        //             _itemWidth = parseFloat(getComputedStyle(_sliderItems[0]).width), // width of one element    
        //             _positionLeftItem = 0, // position of the left active element
        //             _transform = 0, // transformation value .slider_wrapper
        //             _step = _itemWidth / _wrapperWidth * 100, // step size(for transformation)  
        //             _items = []; // elements array

        //         // array filling _items
        //         _sliderItems.forEach(function (item, index) {
        //             _items.push({ item: item, position: index, transform: 0 });
        //         });

        //         var position = {
        //             getItemMin: function () {
        //                 var indexItem = 0;
        //                 _items.forEach(function (item, index) {
        //                     if (item.position < _items[indexItem].position) {
        //                         indexItem = index;
        //                     }
        //                 });
        //                 return indexItem;
        //             },
        //             getItemMax: function () {
        //                 var indexItem = 0;
        //                 _items.forEach(function (item, index) {
        //                     if (item.position > _items[indexItem].position) {
        //                         indexItem = index;
        //                     }
        //                 });
        //                 return indexItem;
        //             },
        //             getMin: function () {
        //                 return _items[position.getItemMin()].position;
        //             },
        //             getMax: function () {
        //                 return _items[position.getItemMax()].position;
        //             }
        //         }

        //         var _transformItem = function (direction) {
        //             var nextItem;
        //             if (direction === 'right') {
        //                 _positionLeftItem++;
        //                 if ((_positionLeftItem + _wrapperWidth / _itemWidth - 1) > position.getMax()) {
        //                     nextItem = position.getItemMin();
        //                     _items[nextItem].position = position.getMax() + 1;
        //                     _items[nextItem].transform += _items.length * 100;
        //                     _items[nextItem].item.style.transform = 'translateX(' + _items[nextItem].transform + '%)';
        //                 }
        //                 _transform -= _step;
        //             }
        //             if (direction === 'left') {
        //                 _positionLeftItem--;
        //                 if (_positionLeftItem < position.getMin()) {
        //                     nextItem = position.getItemMax();
        //                     _items[nextItem].position = position.getMin() - 1;
        //                     _items[nextItem].transform -= _items.length * 100;
        //                     _items[nextItem].item.style.transform = 'translateX(' + _items[nextItem].transform + '%)';
        //                 }
        //                 _transform += _step;
        //             }
        //             _sliderWrapper.style.transform = 'translateX(' + _transform + '%)';
        //         }

        //         //   click event handler for back and forward buttons
        //         var _controlClick = function (e) {
        //             var direction = this.classList.contains('slider__control_right') ? 'right' : 'left';
        //             e.preventDefault();
        //             _transformItem(direction);
        //         };

        //         var _setUpListeners = function () {
        //             // adding a _controlClick handler for the click event to the back and forward buttons
        //             _sliderControls.forEach(function (item) {
        //                 item.addEventListener('click', _controlClick);
        //             });
        //         }

        //         // инициализация
        //         _setUpListeners();

        //         return {
        //             right: function () { // method right
        //                 _transformItem('right');
        //             },
        //             left: function () { // method left
        //                 _transformItem('left');
        //             }
        //         }

        //     }
        // }());

        // var slider = multiItemSlider('.slider')


        // Category Slider
        $(document).ready(function (categorySlider) {

            var slideCount = $('#category-types-slider ul li').length;
            var slideWidth = $('#category-types-slider ul li').width();
            var slideHeight = $('#category-types-slider ul li').height();
            var sliderUlWidth = slideCount * slideWidth;

            $('#category-types-slider').css({ width: slideWidth, height: slideHeight });

            $('#category-types-slider ul').css({ width: sliderUlWidth, marginLeft: - slideWidth });

            $('#category-types-slider ul li:last-child').prependTo('#category-types-slider ul');


            function moveLeft() {
                $('#category-types-slider ul').animate({
                    left: + slideWidth
                }, 200, function () {
                    $('#category-types-slider ul li:last-child').prependTo('#category-types-slider ul');
                    $('#category-types-slider ul').css('left', '');
                });
            };

            function moveRight() {
                $('#category-types-slider ul').animate({
                    left: - slideWidth
                }, 200, function () {
                    $('#category-types-slider ul li:first-child').appendTo('#category-types-slider ul');
                    $('#category-types-slider ul').css('left', '');
                });
            };


            $('.category-arrow-prev').click(function () {
                moveLeft();
            });

            $('.category-arrow-next').click(function () {
                moveRight();
            });


            setTimeout(moveLeft(), 1000); /* works only on load for the first slider...research later*/
        });
    });
