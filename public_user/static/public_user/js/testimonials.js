(function () {
    function getRandom(min, max, times = null) {
        var random_array = [];


//	RANDOM  SINGLE INTEGER FROM RANGE
        if (times === null) return Math.floor(Math.random() * (
            max - min + 1) + min);

//	ARRAY OF RANDOM  MULTIPLE INTEGERS FROM RANGE
        while (times > 0) {
            var random_number = Math.floor(Math.random() * (
                max - min + 1) + min);

            if (random_array.indexOf(random_number) === -1) {

                random_array.push(random_number);
                times--;

            }
        }
        return random_array;

    }

    /*CREATING TESTIMONIALS
    * // created it while developing WAKE-UP-HAPPY SITE
    * https://marcelkolarcik.github.io/wake-up-happy/
    *
    * USING BOOTSTRAP'S CAROUSEL
    *
    * STARTING WITH 4 TESTIMONIALS ON LARGE SCREEN AND DOWNSIZING TO 1 ACCORDING TO SCREEN SIZE
    * EVERY PAGE LOAD WILL DISPLAY DIFFERENT TESTIMONIALS*/
    var classes = [
        "col-xs-6 col-sm-6 col-md-4 col-lg-3  col-xl-3",
        "col-xs-6 col-sm-6 col-md-4 col-lg-3 col-xl-3 d-none d-sm-block",
        "col-xs-6 col-sm-6 col-md-4 col-lg-3 col-xl-3 d-none d-md-block",
        "col-xs-6 col-sm-6 col-md-4 col-lg-3 col-xl-3 d-none d-lg-block"
    ];

    var stars = [
        `	<span class="green"><i class="fas fa-star"></i></span>
						<span class="green"><i class="fas fa-star"></i></span>
						<span class="green"><i class="fas fa-star"></i></span>
						<span><i class="far fa-star"></i></span>
						<span><i class="far fa-star"></i></span>`,
        `	<span class="green"><i class="fas fa-star"></i></span>
						<span class="green"><i class="fas fa-star"></i></span>
						<span class="green"><i class="fas fa-star"></i></span>
						<span class="green"><i class="fas fa-star"></i></span>
						<span><i class="far fa-star"></i></span>`,

        `	<span class="green"><i class="fas fa-star"></i></span>
						<span class="green"><i class="fas fa-star"></i></span>
						<span class="green"><i class="fas fa-star"></i></span>
						<span class="green"><i class="fas fa-star"></i></span>
						<span class="green"><i class="fas fa-star"></i></span>`
    ];


    var testimonials = {

        owner: [
            'The best decision I could ever make, I have achieved over 85% increase in sales in last two years. Highly recommended.'
            ,
            'Very easy to update any details about the website, and I like the fact that you can book additional assistance!'
            ,
            'Ease and efficiency. That\'s all I can say about this site. And extra 14 000 EUR last year....;-)'
            ,
            'You can have new website without leaving your home or office...'
            ,
            'We have upgraded our site and are able to get much higher revenue then before upgrading.'
            ,
            'Marcel was very helpful when we wanted to add extra pages to our website. And now we are reaping benefits of the cooperation.'
            ,
            'Extra income for me and my family. We are selling our homemade goods, and it has been just positive experience so far!'
            ,
            'Using two blogs , both of them about healthy living. And extra cash is going towards our holidays...'
            ,
            'Easy to add the articles, easy to see customers, and easy to earn money ! Recommending very much!'
            ,
            'Great way to make additional income, especially in Ireland, 8 000 EUR ? Yes, please!'
            ,
            'Thinking of getting another blog, as one we already have is really popular!'
            ,
            'If you\'re wanting additional income, look no further!'
        ]

    };

    var names = [
        'J. Edgar',
        'O. Smith',
        'E. Parker',
        'M. Newman',
        'K. Obama',
        'T. Turmam',
        'S. Gretto',
        'A. Schwacke',
        'U. Zajko',
        'I. Noshow',
        'A. Forrest',
        'E. O\'Sullivan'
    ];


    var page_testimonials = testimonials['owner'];


    var img_id = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12];
    // shuffle ( img_id );
    var testi_div = $('#testi_holder');
    var c = -1;
    var b = 0;
    for (var a = 0; a < 12; a++) {

        if (a % 4 === 0) {


            testi_div.append(`<div class="carousel-item ${a === 0 ? 'active' : ''}" data-interval="10000">
	                                  <div class = "row d-flex justify-content-center" id="slide_${a}"></div>
										</div>`);


            for (b = 0; b < 4; b++) {
                c++;

                $('#slide_' + a).append(`
								 <div class="${classes[b]}">
									     <!-- testimonial long -->
							            <div class = "card" >
								            <div class="row no-gutters">

									                <div class = "d-flex justify-content-around align-items-end" >

				<img src="https://marcellidesigns.s3.amazonaws.com/static/public/images/avatars/${img_id[c]}.png" 
									                class="avatar" alt="avatar image">

										                <div>
											               ${stars[getRandom(0, 2)]}
										                </div>

									                </div >

									                <div class = "card-body" >

									                <span class="float-right">
									                <span class = "blockquote-footer" >
									                      ${names[c]}
									                    </span >

									                 </span>
									               <hr class="bg_green">

									             <h3 class = "nav_link_property" >${page_testimonials[c].substring(
                    0, 20)} ...</h3 >

									                    <p class = "card-text quote_text" >
									                        <span class = "quote_mark" >“</span >
									                   <cite>${page_testimonials[c]}</cite>
									                        <span class = "quote_mark" >“</span >
									                    </p >

									                </div >

								            </div>
							            </div >
									     <!--end of testimonial long -->
								  </div>
								`);
            }
        }


    }

})()