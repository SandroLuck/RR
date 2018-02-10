$.ajaxSetup({ cache: true, timeout: 10000 });

function is_numeric(n)
{
	return !isNaN(parseFloat(n)) && isFinite(n);
}
	
function bucks(x)
{
	return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".");
}

function share(link, title)
{
	if(id < 2000000000 && window.location != window.parent.location)
	{
		VK.init(function() {
			VK.api("getUserSettings", {}, function(data) {
				if(data.response&8199)
				{
					VK.api("wall.post", {message: title + ' http://vk.com/app3201433?ad_id=go_' + link, attachments: 'photo192852686_309924728,http://vk.com/app3201433?ad_id=go_' + link});
				} 
				else
				{
					VK.callMethod('showSettingsBox',8199);
				}
			});
		});
	}

	if(id < 2000000000 && window.location == window.parent.location)
	{
		var win=window.open('//vk.com/share.php?url=http://rivalregions.com/slide/go/' + link.replace('/', '_').replace('/', '_').replace('/', '_').replace('/', '_').replace('/', '_').replace('/', '_').replace('/', '_'), '', "location,width=400,height=300,top=0");
  		win.focus();
	}

	if(pl	==	'mm')
	{
		mailru.loader.require('api', function () { 
			mailru.app.init('315a2bfa94f55decb4b57ec7893b5d3c');
			mailru.common.stream.post({'title': mm_title, 'text': title, 'img_url': 'http://rivalregions.com/static/images/mm.jpg'});
		});
	}

	if(pl	==	'fb')
	{
		FB.ui({
		  quote: title,
		  method: 'share',
		  href: 'http://rivalregions.com',
		  picture: 'http://rivalregions.com/static/avatars/big/186/192852686_1431370239.png',
		}, function(response){});
	}

	if(pl	==	'ok')
	{
		share_title_ok	=	title;
		$.ajax({
			url: '/ok/index/1/1',
			type: 'post',
			data: {m: title, c : (new Date()).getTime()},
			success: function(d) {
				FAPI.UI.showConfirmation('stream.publish', share_title_ok, d);
			}
		});
	}
}

function robo(p)
{
	$.ajax({
		dataType: "html",
        type: "GET",
        data : {phone: $('input[name="phone"]').val(), c : (new Date()).getTime()},
        url: '/main/set_rk/' + p,
		success: function(data) {
			var data = jQuery.parseJSON(data);
			$('input[name="txn_id"]').val(data.txn_id);
			$('input[name="summ"]').val(data.summ);
			$('input[name="to"]').val($('input[name="phone"]').val());
			$('#slide_add_robo').submit();
		}
	});
}

var last_w_unit = 1;

/* bar coloring */
function bar_color(n)
{
	bar_color_n	=	hp
	bar_color_c	=	1;
	var ns	=	n;
	if(n	<=	4)
	{
		n	=	5;
	}
	if($('#header_my_avatar_big').attr('now')	==	'1')
	{
		bar_color_c	=	2;
	}

	if(n*1 < hp*1)
	{
		$('#header_my_fill_bar').fadeIn(200);
	}

	if(n*1 > 10)
	{
		$('.w_add_not_enough').remove();
	}
	
	$('#s, #s_index').html(ns);
	$('#header_my_bar').css('background-color', 'rgba(' + Math.round((255*(bar_color_n-n))/bar_color_n) + ',' + Math.round((255*n)/bar_color_n) + ',0,0.9)');
	$('#header_my_bar_data, .work_stamina, #s_index').css('color', 'rgba(' + Math.round((255*(bar_color_n-n))/bar_color_n) + ',' + Math.round((255*n)/bar_color_n) + ',0,0.9)');
	$('#header_my_bar_close').css('height', bar_color_c*Math.round(((bar_color_n-n)/2)*(100/bar_color_n)) + 'px');
	
	$('.war_w_unit_div[url="' + last_w_unit + '"]').click();
}

function refresh_hp()
{
	$.ajax({
		dataType: "html",
        type: "GET",
        data : {c : (new Date()).getTime()},
        url: '/main/get_hp',
		success: function(data) {
			var data = jQuery.parseJSON(data);
			if(data.hp != undefined)
			{
				if(data.hp != $('#s').html())
				{
					bar_color(data.hp);
					if(data.hp < hp)
					{
						$('#header_my_fill_bar').fadeIn(200);
						$('#header_stamina').html('+' + data.plus + ' ' + data.stamina_in + ' <span class="header_stamina_counter"></span>');
						$('.header_stamina_counter').countdown({onExpiry: function() {
							$('#header_stamina').html(data.stamina_now + '...');
							setTimeout(function() { refresh_hp(); }, 6000);
						}, until: (data.next_time+2), layout: '{mnn}:{snn}'});
					}
					else
					{
						$('#header_stamina').html('');
						$('#header_my_fill_bar, .header_my_fill_bar_area').fadeOut(200);
					}
				}
			}
		}
	});
}
refresh_hp();

function level_up()
{

}

function exp_size(n, l)
{
	$('#index_exp_points').html(n);
	$('#index_exp_level').html(l);
	

	var n_exp_check	=	500;
	var i_exp_check	=	1;

	while(true)
	{
		n_exp_check	+=	Math.round(n_exp_check*0.2);
		if(i_exp_check >= l)
		{
			break;
		}
		i_exp_check++;
	}

	var n_exp_check_2	=	500;
	var i_exp_check_2	=	1;

	while(true)
	{
		if(i_exp_check_2 >= l)
		{
			break;
		}

		n_exp_check_2	+=	Math.round(n_exp_check_2*0.2);
		
		i_exp_check_2++;
	}

	$('.my_expbar_width').css('width', Math.round(100*(n-n_exp_check_2)/(n_exp_check-n_exp_check_2)) + '%');
	$('.my_expbar_exp').html(l);
	$('#header_my_expbar_big, #header_my_expbar').attr('title', '').removeClass('tip');
}

function add_messages()
{
	$('#message_menu').addClass('green_bg');
}

function add_subs()
{
	$('#news_menu').addClass('green_bg');
}

function remove_messages()
{
	$('#message_menu').removeClass('green_bg');
}

function remove_subs()
{
	$('#news_menu').removeClass('green_bg').removeClass('red_bg');
}

function add_party(n, party_id)
{
	$('#party_menu_members').attr('action', 'listed/party/' + party_id)
	$('#party_menu_party_vote').html('').fadeOut(1);
	$('#party_menu_parliament_vote').html('').fadeOut(1);
	remove_messages();
	if(n	!=	'0')
	{
		$('#party_menu_members').attr('n', n).html('&nbsp;+'	+	n).fadeIn();
	}
	else
	{
		$('#party_menu_members').fadeOut();
	}
}

function add_parliament_vote(region_id)
{
	$('#party_menu_parliament_vote').attr('action', 'elections/parliament/' + region_id).html('&nbsp;&#10004;').fadeIn();
}

function add_party_vote(party_id)
{
	$('#party_menu_party_vote').attr('action', 'elections/party/' + party_id).html('&nbsp;&#10004;').fadeIn();
}

function no_refill()
{
	$.ajax({
		dataType: "html",
        type: "GET",
        data : {c : (new Date()).getTime()},
        url: '/main/get_refill',
		success: function(data) {
			$('#refill_delay').html(data).animate({opacity: 0}, 200, function() {
				$(this).animate({opacity: 1}, 200,  function() {
					$(this).animate({opacity: 0}, 200, function() {
						$(this).animate({opacity: 1}, 200);
					});
				});
			});
		}
	});
}

function no_money()
{
	$('#money').animate({opacity: 0}, 200, function() {
		$(this).animate({opacity: 1}, 200,  function() {
			$(this).animate({opacity: 0}, 200, function() {
				$(this).animate({opacity: 1}, 200);
			});
		});
	});
}

function no_gold()
{
	$('#gold').animate({opacity: 0}, 200, function() {
		$(this).animate({opacity: 1}, 200,  function() {
			$(this).animate({opacity: 0}, 200, function() {
				$(this).animate({opacity: 1}, 200);
			});
		});
	});
}

function no_hp()
{
	$('#header_my_bar_inner').animate({opacity: 0}, 300, function() {
		$(this).animate({opacity: 1}, 300,  function() {
			$(this).animate({opacity: 0}, 300, function() {
				$(this).animate({opacity: 1}, 300,  function() {
					$(this).animate({opacity: 0}, 300, function() {
						$(this).animate({opacity: 1}, 300);
					});
				});
			});
		});
	});

	$('#header_my_fill_bar').animate({opacity: 0}, 300, function() {
		$(this).animate({opacity: 1}, 300,  function() {
			$(this).animate({opacity: 0}, 300, function() {
				$(this).animate({opacity: 1}, 300,  function() {
					$(this).animate({opacity: 0}, 300, function() {
						$(this).animate({opacity: 1}, 300);
					});
				});
			});
		});
	});
}

function new_m(m)
{
	if($('#m').html() != m)
	{
		if(m == '&#48;')
		{
			m =	'0';
		}

		m = m.split('.').join("");
		m = m*1;
		var m_old	=	$('#m').html();
		m_old = m_old.split('.').join("");
		m_old = m_old*1;

		var comma_separator_number_step = $.animateNumber.numberStepFactories.separator('.')
		$('#m').prop('number', m_old).animateNumber(
		  {
		    number: m,
		    numberStep: comma_separator_number_step
		  },
		  2000
		);
	}
}

function new_g(mg)
{
	if($('#g').html() != mg)
	{
		if(mg == '&#48;')
		{
			mg =	'0';
		}

		mg = mg.split('.').join("");
		mg = mg*1;
		var mg_old	=	$('#g').html();
		mg_old = mg_old.split('.').join("");
		mg_old = mg_old*1;

		var comma_separator_number_step = $.animateNumber.numberStepFactories.separator('.')
		$('#g').prop('number', mg_old).animateNumber(
		  {
		    number: mg,
		    numberStep: comma_separator_number_step
		  },
		  2000
		);
	}
}

function check_width()
{
	var tmp_width	=	Math.round($(window).width()/100);

	if(Math.round($(window).height()-$('#header_content').height()) < 590)
	{
		$('#lower_state').hide();
	}
	else
	{
		$('#lower_state').show();
	}

	if(!setup[8] || !setup[9])
	{
		var tmp_width	=	tmp_width + '&setup_8=' + setup[8] + '&setup_9=' + setup[9];
	}
	
	$('#content').css('margin-left', Math.round(($(window).width()-800)/2)+'px');
	$('link[url="icons"]').attr('href', static_url + 'icons.theme?icons=' + theme[9] + '&width=' + tmp_width);

	if(!setup[8])
	{
		var tmp_width	=	8;
	}
	else
	{
		var tmp_width	=	Math.round($(window).width()/100);
	}
	
	if(tmp_width	>	13)
	{
		$('#header_my_avatar').attr('now', '0');
		$('#header_my_avatar_big').attr('now', '1');

		if(setup[8])
		{
			$('.header_logo').css('margin-left', '-220px')
						 	  .css('width', '420px')
						 	  .css('font-size', '48px')
						 	  .css('padding-top', '20px');
		}
	}
	else
	{
		$('#header_my_avatar_big').attr('now', '0');
		$('#header_my_avatar').attr('now', '1');
		$('.header_logo').css('margin-left', '-110px')
						 	  .css('width', '220px')
						 	  .css('font-size', '24px')
						 	  .css('padding-top', '10px');
	}
	
	if($('#header_my_avatar').css('display')	!=	'none'	||	$('#header_my_avatar_big').css('display')	!=	'none')
	{
		if(tmp_width	>	13)
		{
			$('#header_my_avatar').css('display', 'none');
			$('#header_my_avatar_big').css('display', 'block');
		}
		else
		{
			$('#header_my_avatar_big').css('display', 'none');
			$('#header_my_avatar').css('display', 'block');
		}
	}

	if($('#header_my_expbar').css('display')	!=	'none'	||	$('#header_my_expbar_big').css('display')	!=	'none')
	{
		if(tmp_width	>	13)
		{
			$('#header_my_expbar').css('display', 'none');
			$('#header_my_expbar_big').css('display', 'block');
		}
		else
		{
			$('#header_my_expbar_big').css('display', 'none');
			$('#header_my_expbar').css('display', 'block');
		}
	}

	var tmp_width	=	Math.round($(window).width());
	var tmp_height	=	Math.round($(window).height());

	$('#map_under').css('width', Math.round(tmp_width) + 'px')
				   .css('margin-left', -Math.round((tmp_width-800)/2) + 'px');
	$('#map_cache_all').css('width', Math.round(tmp_width) + 'px')
				   .css('height', Math.round(tmp_height) + 'px')
				   .css('margin-left', -Math.round((tmp_width-800)/2) + 'px')
				   .css('margin-top', '-50px');
}

function guide_show(url, text, deg, top, left)
{
	$('#header_slide_inner').append('<div class="guide_show" url="' + url + '"><img width="32" height="32" src="/static/images/icons/' + theme[9] + '/arrowguide.png" class="guide_show_arrow float_left" url="' + url + '"><div class="float_left guide_show_text">' +  text + '</div></div>');
	$('.guide_show[url=' + url + ']').css('top', top + 'px')
		.css('margin-left', left + 'px').show(800);

	$('.guide_show_arrow[url=' + url + ']').css('-moz-transform', 'rotate(' + deg + 'deg)')
	    .css('-webkit-transform', 'rotate(' + deg + 'deg)')
	    .css('-o-transform', 'rotate(' + deg + 'deg)')
	    .css('-ms-transform', 'rotate(' + deg + 'deg)');
}

function guide_show_in(url, text, deg, top, left)
{
	$('.guided_content').append('<div class="guide_show" url="' + url + '"><img width="32" height="32" src="/static/images/icons/' + theme[9] + '/arrowguide.png" class="guide_show_arrow float_left" url="' + url + '"><div class="float_left guide_show_text">' +  text + '</div></div>');
	$('.guide_show[url=' + url + ']').css('top', top + 'px')
		.css('margin-left', left + 'px').show(800);

	$('.guide_show_arrow[url=' + url + ']').css('-moz-transform', 'rotate(' + deg + 'deg)')
	    .css('-webkit-transform', 'rotate(' + deg + 'deg)')
	    .css('-o-transform', 'rotate(' + deg + 'deg)')
	    .css('-ms-transform', 'rotate(' + deg + 'deg)');
}

function full_on()
{
	var doc = document.body;
	if (doc.requestFullscreen) {
		doc.requestFullscreen();
		$('body').css('width', '100%').css('height', '100%');
		$('#header_fullscreen').removeClass('fullscreen_on').addClass('fullscreen_off');
	}
	else if (doc.mozRequestFullScreen) {
		doc.mozRequestFullScreen();
		$('body').css('width', '100%').css('height', '100%');
		$('#header_fullscreen').removeClass('fullscreen_on').addClass('fullscreen_off');
	}
	else if (doc.webkitRequestFullScreen) {
		doc.webkitRequestFullScreen();
		$('body').css('width', '100%').css('height', '100%');
		$('#header_fullscreen').removeClass('fullscreen_on').addClass('fullscreen_off');
	}
}

function switch_back_hash(n)
{
	switch(n)
	{
		case 'overview':
			return 'main/content';
		break;

		case 'messages':
			return 'main/messages';
		break;

		case 'listed/hospital':
			n	=	'listed/country/0/0/hospital';
		break;

		case 'listed/school':
			n	=	'listed/country/0/0/school';
		break;

		case 'listed/military':
			n	=	'listed/country/0/0/military';
		break;

		default:
			n	=	n.replace('map/country/', 'map/index/0/');
			n	=	n.replace('war/join/', 'war/create/0/0/0/');
			n	=	n.replace('state/details/', 'map/state_details/');
			n	=	n.replace('autonomy/details/', 'map/autonomy_details/');
			n	=	n.replace('party/new', 'party/pre_create');
			n	=	n.replace('messages/', 'slide/chat/user_');
			n	=	n.replace('battle/', 'war/index/');
		break;
	}

	return n;
}

function print_r(o)
{
	return JSON.stringify(o,null,'\t').replace(/\n/g,'').replace(/\t/g,' '); 
}

function hash_return(n)
{
	switch(n)
	{
		case 'main/content':
			n	=	'overview';
		break;

		case 'main/messages':
			n	=	'messages';
		break;

		case 'listed/country/0/0/hospital':
			n	=	'listed/hospital';
		break;

		case 'listed/country/0/0/school':
			n	=	'listed/school';
		break;

		case 'listed/country/0/0/military':
			n	=	'listed/military';
		break;

		default:
			n	=	n.replace('map/index/0/', 'map/country/');
			n	=	n.replace('war/create/0/0/0/', 'war/join/');
			n	=	n.replace('map/state_details/', 'state/details/');
			n	=	n.replace('map/autonomy_details/', 'autonomy/details/');
			n	=	n.replace('party/pre_create', 'party/new');
			n	=	n.replace('slide/chat/user_', 'messages/');
			n	=	n.replace('war/index/', 'battle/');
		break;
	}
	return n;
}

function hash_place(n)
{
	document.location.hash = hash_return(n) + hash_after;
}

var last_before_slide	=	'main/content';

var antiflood_navigation=	new Array();
function clear_antiflood_navigation()
{
	antiflood_navigation	=	new Array();
}
var clear_interval_navigation=self.setInterval( function(){ clear_antiflood_navigation() }, 1000);

function slide_header(n)
{
	if(n != undefined)
	{
		if(antiflood_navigation.indexOf(n) <= -1)
		{
			if(typeof(socket) != "undefined")
			{
				socket.$events	=	0;
			}

			antiflood_navigation.push(n);
			$('#l_image_target').imgAreaSelect({remove:true});
		    var tmp = $(location).attr('href').split('.com/#');
			var tmp2 = $(location).attr('href').split('.com');
			if(tmp[1] != undefined || tmp2[1]	==	'/' || tmp2[1]	==	'')
			{
				$('.switch_help').remove();
				$.ajax({
					dataType: "html",
			        type: "GET",
			        data : {c : (new Date()).getTime()},
			        url: '/'	+	n,
					success: function(data) {
						if(data	==	'no_hp')
						{
							no_hp();
						}
						else
						{
							$('.switch_help').remove();
							$('#header_slide_inner').animate({
								opacity: 0
							}, 200, function() {
								$('#header_slide_inner').html(data).animate({
									opacity: 1,
								}, 200, function(){
									$('.tip').tipTip();
								});
								$('#header_slide').animate({
									opacity: 1,
									height: '100%'
								}, 300);
								hash_place(n);
							});

							$('.note_tip').fadeOut(50, function() {
								$('.note_tip').remove();
							});
						}
					}
				});
			}
			else
			{
				window.location	=	"/#" + hash_return(n);
			}
		}
	}
}

function ajax_action(x, no_hash)
{
	$('body').css('overflow-y', 'hidden');
	if(x != undefined)
	{
		//var iframe = document.getElementById('appboost');
		//iframe.src = iframe.src;
		if(antiflood_navigation.indexOf(x) <= -1)
		{
			if(typeof(socket) != "undefined")
			{
				socket.$events	=	0;
			}

			antiflood_navigation.push(x);
			$('#slide_close').click();
			$('#l_image_target').imgAreaSelect({remove:true});
			last_before_slide	=	x;
			window.last_action	=	window.this_action;
			window.this_action	=	x;

			var tmp = $(location).attr('href').split('.com/#');
			var tmp2 = $(location).attr('href').split('.com');
			if(tmp[1] != undefined || tmp2[1]	==	'/' || tmp2[1]	==	'')
			{
				$('.move_progress').remove();
				
				$('.note_tip').fadeOut(50, function() {
					$('.note_tip').remove();
				});

				$('.switch_help').remove();
				
					$.ajax({
						dataType: "html",
				        type: "GET",
				        data : {c : (new Date()).getTime()},
				        url: '/' + x,
						success: function(data) {
							$('#content').fadeOut(100, function() {
								$('#content').html('').html(data).fadeIn(200, function(){
									$('.tip').tipTip();
								});
								if(no_hash == undefined)
								{
									hash_place(x);
								}

								if(x.indexOf("map") === -1 && (pl != 'vk' || window.location == window.parent.location))
								{
									place_ads();
								}
							});
						}
					});
			}
			else
			{
				window.location	=	"/#" + hash_return(x);
			}
		}
	}
}

function hash_action(n)
{
	n	=	switch_back_hash(n);
	/* slides */
	if(
			n.indexOf("slide/") !== -1
		 || n.indexOf("log") !== -1
		 || n.indexOf("admin") !== -1
		 || n.indexOf("work/go/") !== -1
		 || n.indexOf("work/change") !== -1
		 || n.indexOf("map/details/") !== -1
		 || n.indexOf("parliament/law/") !== -1
		 || n.indexOf("newspaper/create") !== -1
		 || n.indexOf("newspaper/show") !== -1
		 || n.indexOf("blocs/create") !== -1
		 || n.indexOf("blocs/show") !== -1
		 || n.indexOf("blocs/elect") !== -1
		 || n.indexOf("blocs/all") !== -1
		 || n.indexOf("newspaper/all") !== -1
		 || n.indexOf("listed/") !== -1
		 || n.indexOf("party/pre_create") !== -1
		 || n.indexOf("parliament/offer") !== -1
		 || n.indexOf("storage/house") !== -1
		 || n.indexOf("main/moderator") !== -1
		 || n.indexOf("elections/") !== -1
		 || n.indexOf("leader/requests") !== -1
		 || n.indexOf("rival/awards") !== -1
		 || n.indexOf("rival/award") !== -1
		 || n.indexOf("auction/show") !== -1
		 || n.indexOf("graph/") !== -1
		 || (n.indexOf("factory/") !== -1 && n.indexOf("factory/edit") === -1)
		 || n.indexOf("news/write") !== -1
		 || n.indexOf("news/ask") !== -1
		 || n.indexOf("news/comments") !== -1
		 || n.indexOf("news/votes") !== -1
		 || n.indexOf("guide/slide") !== -1
		 || n.indexOf("war/details") !== -1
		 || n.indexOf("war/day") !== -1
		 || n.indexOf("war/in") !== -1
		 || n.indexOf("state_details") !== -1
		 || n.indexOf("autonomy_details") !== -1
		 || n.indexOf("party/message") !== -1
		 || n.indexOf("war/all") !== -1
		 || n.indexOf("war/bloc") !== -1
		 || n.indexOf("war/train") !== -1
		 || n.indexOf("war/damage") !== -1
		 || n.indexOf("war/create") !== -1
		 || n.indexOf("war/top") !== -1
		 || n.indexOf("news/edit") !== -1
		 || n.indexOf("guide") !== -1
		 || n.indexOf("auction/all") !== -1
	)
	{
		/* deside what to send under slider, no hash_place */
		hash_action_default	=	'main/content';
		if(n.indexOf("work/") !== -1)
		{
			hash_action_default	=	'work';
		}

		if(n.indexOf("war_") !== -1)
		{
			hash_action_default	=	'war';
		}

		if(n.indexOf("war/details") !== -1)
		{
			hash_action_default	=	'war';
		}

		if(n.indexOf("slide/conference") !== -1)
		{
			hash_action_default	=	'news';
		}

		if(n.indexOf("slide/chat/user_") !== -1)
		{
			hash_action_default	=	'main/messages';
		}

		if(n.indexOf("news/comments") !== -1)
		{
			hash_action_default	=	'news';
		}

		if(n.indexOf("parliament/law") !== -1)
		{
			hash_action_default	=	'parliament';
		}
		
		ajax_action(hash_action_default, 1);
		if(hash_action_default.indexOf("map") === -1 && (pl != 'vk' || window.location == window.parent.location))
		{
			place_ads();
		}
		slide_header(n);
	}
	else
	{
		ajax_action(n);
		if(n.indexOf("map") === -1 && (pl != 'vk' || window.location == window.parent.location))
		{
			place_ads();
		}
	}
}

function show_context()
{

}

function start_block(a)
{
	window.start_time	=	new Date().getTime();
	$('body').append('<div id="block"></div>');
	$('#' + ajax_block).fadeOut(0, function () {$('#header_ajax').fadeIn(0);});
}

function stop_block(a)
{
	window.end_time	=	new Date().getTime();
	$('#developers_data').html(window.end_time-window.start_time + 'ms');
	$('#block').remove();
	$('#header_ajax').fadeOut(0, function () {$('#' + ajax_block).fadeIn(0);});
}

function c()
{
	return (new Date()).getTime()
}

var ajax_block	=	'header_money';

$(document).ready(function() {
	/* no vk fb frame */
	$('#header_my_fill_bar').click(function(event){if(event.which==2){event.stopImmediatePropagation();}}).click(function(){
		var tmp	=	0;

		$.ajax({
			url: '/main/energy_fill',
			data: {c : (new Date()).getTime()},
			success: function(data) {
				if(data	==	'no_money')
				{
					$('div[action="storage"]').animate({opacity: 0}, 200, function() {
						$(this).animate({opacity: 1}, 200,  function() {
							$(this).animate({opacity: 0}, 200, function() {
								$(this).animate({opacity: 1}, 200);
							});
						});
					});

					if(confirm($('#header_my_fill_bar').attr('noen')))
		    		{
		    			ajax_action('storage/index/energy');
					}
				}
				else
				{
					if(data	==	'no')
					{
						$('#header_my_fill_bar_countdown').animate({opacity: 0}, 200, function() {
							$(this).animate({opacity: 1}, 200,  function() {
								$(this).animate({opacity: 0}, 200, function() {
									$(this).animate({opacity: 1}, 200);
								});
							});
						});
					}
					else
					{
						$('#header_my_fill_bar').append(data);
					}
				}
			}
		});
	});

	$(document).on('mousedown', function(e) { 
		if(e.which == 2 && window.location == window.parent.location)
		{
			e.preventDefault();
			if($(e.target).attr('action')	!=	undefined)
			{
				window.open('/#' + $(e.target).attr('action'));
			}
   		}

   		if(e.which == 3)
		{
			e.preventDefault();
			/* контекст */
			show_context();
   		}
   	});

   	$('.header_logo_inner').on('mousedown', function(e){
		e.preventDefault();
		ajax_action($(this).attr('action'));
		$('#slide_close').click();
	});

	/* hash navigating */
	var path = $(location).attr('href').split('#');
	if(path[1]	!=	undefined && path[1] != 'overview')
	{
		hash_action(path[1]);
	}

	$(window).resize(function() {
		check_width();
	});

	check_width();
	
	$('#message_menu').click(function(event){if(event.which==2){event.stopImmediatePropagation();}}).click(function(){
		ajax_action('main/messages');
	});

	$('#auction_menu').click(function(event){if(event.which==2){event.stopImmediatePropagation();}}).click(function(){
		slide_header('auction/all');
	});

	$('#news_menu[action="news"]').click(function(event){if(event.which==2){event.stopImmediatePropagation();}}).click(function(){
		ajax_action('news');
	});

	$('#header_my_bar').hover(function() {
		$('#money, #gold, #header_my_exp_data').fadeOut(0, function() {
			$('#header_my_bar_data').fadeIn(0);
		});
	}, function() {
		$('#header_my_bar_data').fadeOut(0, function() {
			$('#money, #gold').fadeIn(0);
		});
	});

	/* ajax_action */
	$('.ajax_action').click(function(event){if(event.which==2){event.stopImmediatePropagation();}}).click(function(){
		ajax_action($(this).attr('action'));
	});
	
	/* reload */
	$('#reload_menu').click(function(event){if(event.which==2){event.stopImmediatePropagation();}}).click(function(){
		if(typeof window.this_action == 'undefined')
		{
			window.this_action	=	'main/content';
		}
		$('#content').load('/' + window.this_action + '?c=' + (new Date()).getTime() + '#content', function(){
			$('.tip').tipTip();
		});
	});
	
	/* back */
	$('#back_menu').click(function(event){if(event.which==2){event.stopImmediatePropagation();}}).click(function(){
		$('#content').load('/' + window.last_action + '#content', function(){
			$('.tip').tipTip();
		});
		if(typeof window.this_action == 'undefined')
		{
			window.this_action	=	'main/content';
			window.last_action	=	'main/content';
		}
		tmp	=	window.last_action;
		window.last_action	=	window.this_action;
		window.this_action	=	tmp;
	});
	
	/* blocking */
	$(document).ajaxStart(function(){
		start_block();
	});
	$(document).ajaxStop(function(){
		stop_block();
	});
	$(document).ajaxError(function(){
		stop_block();
	});
	
	$('#header_money').click(function (){
		slide_header('slide/money');
	});

	/* sliding */
	$('.header_slide').click(function(event){if(event.which==2){event.stopImmediatePropagation();}}).click(function(){
		slide_header($(this).attr('action'));
	});
	
	$('.header_slide_common').click(function(event){if(event.which==2){event.stopImmediatePropagation();}}).click(function(){
		slide_header($(this).attr('action'));
	});
	$('#money, #gold').click(function(event){if(event.which==2){event.stopImmediatePropagation();}}).click(function (){
		slide_header('log/index/money');
	});
	
	$('#header_fullscreen').click(function(event){if(event.which==2){event.stopImmediatePropagation();}}).click(function(){
		if($('#header_fullscreen').hasClass('fullscreen_on'))
		{
			full_on()
		}
		else
		{
			if (document.exitFullscreen) {
				document.exitFullscreen();
				$('#header_fullscreen').removeClass('fullscreen_off').addClass('fullscreen_on');
				$('body').css('width', '100%').css('height', '100%');
			}
			else if (document.mozCancelFullScreen) {
				document.mozCancelFullScreen();
				$('#header_fullscreen').removeClass('fullscreen_off').addClass('fullscreen_on');
				$('body').css('width', '100%').css('height', '100%');
			}
			else if (document.webkitCancelFullScreen) {
				document.webkitCancelFullScreen();
				$('#header_fullscreen').removeClass('fullscreen_off').addClass('fullscreen_on');
				$('body').css('width', '100%').css('height', '100%');
			}
		}
	});
});