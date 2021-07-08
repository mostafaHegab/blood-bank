/**
 * /* to validate input phone to accept only number
 *
 * @format
 */

console.log(document.forms[0]);
$("input[id='form1']").on('input', function () {
	$("input[id='form2']").val(destroyMask(this.value));
	this.value = createMask($("input[id='form2']").val());
});

function createMask(string) {
	return string.replace(/(\d{3})(\d{3})(\d{3})/, '$1-$2-$3');
}

function destroyMask(string) {
	return string.replace(/\D/g, '').substring(0, 9);
}

/*---------------to show governerate and cities in selecct option------------------- */
var governerate = [
	{
		id: '1',
		governorate_name_en: 'Cairo',
	},
	{
		id: '2',
		governorate_name_en: 'Giza',
	},
	{
		id: '3',
		governorate_name_en: 'Alexandria',
	},
	{
		id: '4',
		governorate_name_en: 'Dakahlia',
	},
	{
		id: '5',
		governorate_name_en: 'Red Sea',
	},
	{
		id: '6',
		governorate_name_en: 'Beheira',
	},
	{
		id: '7',
		governorate_name_en: 'Fayoum',
	},
	{
		id: '8',
		governorate_name_en: 'Gharbiya',
	},
	{
		id: '9',
		governorate_name_en: 'Ismailia',
	},
	{
		id: '10',
		governorate_name_en: 'Menofia',
	},
	{
		id: '11',
		governorate_name_en: 'Minya',
	},
	{
		id: '12',
		governorate_name_en: 'Qaliubiya',
	},
	{
		id: '13',
		governorate_name_en: 'New Valley',
	},
	{
		id: '14',
		governorate_name_en: 'Suez',
	},
	{
		id: '15',
		governorate_name_en: 'Aswan',
	},
	{
		id: '16',
		governorate_name_en: 'Assiut',
	},
	{
		id: '17',
		governorate_name_en: 'Beni Suef',
	},
	{
		id: '18',
		governorate_name_en: 'Port Said',
	},
	{
		id: '19',
		governorate_name_en: 'Damietta',
	},
	{
		id: '20',
		governorate_name_en: 'Sharkia',
	},
	{
		id: '21',
		governorate_name_en: 'South Sinai',
	},
	{
		id: '22',
		governorate_name_en: 'Kafr Al sheikh',
	},
	{
		id: '23',
		governorate_name_en: 'Matrouh',
	},
	{
		id: '24',
		governorate_name_en: 'Luxor',
	},
	{
		id: '25',
		governorate_name_en: 'Qena',
	},
	{
		id: '26',
		governorate_name_en: 'North Sinai',
	},
	{
		id: '27',
		governorate_name_en: 'Sohag',
	},
];
var cairo_cities = [
	{
		id: '1',
		city_name_en: '15 May',
	},

	{
		id: '2',
		city_name_en: 'Al Azbakeyah',
	},
	{
		id: '3',
		city_name_en: 'Al Basatin',
	},
	{
		id: '4',
		city_name_en: 'Tebin',
	},
	{
		id: '5',
		city_name_en: 'El-Khalifa',
	},
	{
		id: '6',
		city_name_en: 'El darrasa',
	},
	{
		id: '7',
		city_name_en: 'Aldarb Alahmar',
	},
	{
		id: '8',
		city_name_en: 'Zawya al-Hamra',
	},
	{
		id: '9',
		city_name_en: 'El-Zaytoun',
	},
	{
		id: '10',
		city_name_en: 'Sahel',
	},
	{
		id: '11',
		city_name_en: 'El Salam',
	},
	{
		id: '12',
		city_name_en: 'Sayeda Zeinab',
	},
	{
		id: '13',
		city_name_en: 'El Sharabeya',
	},
	{
		id: '14',
		city_name_en: 'Shorouk',
	},
	{
		id: '15',
		city_name_en: 'El Daher',
	},
	{
		id: '16',
		city_name_en: 'Ataba',
	},
	{
		id: '17',
		city_name_en: 'New Cairo',
	},
	{
		id: '18',
		city_name_en: 'El Marg',
	},
	{
		id: '19',
		city_name_en: 'Ezbet el Nakhl',
	},
	{
		id: '20',
		city_name_en: 'Matareya',
	},
	{
		id: '21',
		governorate_id: '1',
		city_name_ar: 'المعادى',
		city_name_en: 'Maadi',
	},
	{
		id: '22',
		city_name_en: 'Maasara',
	},
	{
		id: '23',
		city_name_en: 'Mokattam',
	},
	{
		id: '24',
		city_name_en: 'Manyal',
	},
	{
		id: '25',
		city_name_en: 'Mosky',
	},
	{
		id: '26',
		city_name_en: 'Nozha',
	},
	{
		id: '27',
		city_name_en: 'Waily',
	},
	{
		id: '28',
		city_name_en: 'Bab al-Shereia',
	},
	{
		id: '29',
		city_name_en: 'Bolaq',
	},
	{
		id: '30',
		city_name_en: 'Garden City',
	},
	{
		id: '31',
		city_name_en: 'Hadayek El-Kobba',
	},
	{
		id: '32',
		city_name_en: 'Helwan',
	},
	{
		id: '33',
		city_name_en: 'Dar Al Salam',
	},
	{
		id: '34',
		city_name_en: 'Shubra',
	},
	{
		id: '35',
		city_name_en: 'Tura',
	},
	{
		id: '36',
		city_name_en: 'Abdeen',
	},
	{
		id: '37',
		city_name_en: 'Abaseya',
	},
	{
		id: '38',
		city_name_en: 'Ain Shams',
	},
	{
		id: '39',
		city_name_en: 'Nasr City',
	},
	{
		id: '40',
		city_name_en: 'New Heliopolis',
	},
	{
		id: '41',
		city_name_en: 'Masr Al Qadima',
	},
	{
		id: '42',
		city_name_en: 'Mansheya Nasir',
	},
	{
		id: '43',
		city_name_en: 'Badr City',
	},
	{
		id: '44',
		city_name_en: 'Obour City',
	},
	{
		id: '45',
		city_name_en: 'Cairo Downtown',
	},
	{
		id: '46',
		city_name_en: 'Zamalek',
	},
	{
		id: '47',
		city_name_en: 'Kasr El Nile',
	},
	{
		id: '48',
		city_name_en: 'Rehab',
	},
	{
		id: '49',
		city_name_en: 'Katameya',
	},
	{
		id: '50',
		city_name_en: 'Madinty',
	},
	{
		id: '51',
		city_name_en: 'Rod Alfarag',
	},
	{
		id: '52',
		city_name_en: 'Sheraton',
	},
	{
		id: '53',
		city_name_en: 'El-Gamaleya',
	},
	{
		id: '54',
		city_name_en: '10th of Ramadan City',
	},
	{
		id: '55',
		city_name_en: 'Helmeyat Alzaytoun',
	},
	{
		id: '56',
		city_name_en: 'New Nozha',
	},
	{
		id: '57',
		city_name_en: 'Capital New',
	},
];

var Giza_cities = [
	{
		id: '58',
		city_name_en: 'Giza',
	},
	{
		id: '59',
		city_name_en: 'Sixth of October',
	},
	{
		id: '60',
		city_name_en: 'Cheikh Zayed',
	},
	{
		id: '61',
		city_name_en: 'Hawamdiyah',
	},
	{
		id: '62',
		city_name_en: 'Al Badrasheen',
	},
	{
		id: '63',
		city_name_en: 'Saf',
	},
	{
		id: '64',
		city_name_en: 'Atfih',
	},
	{
		id: '65',
		city_name_en: 'Al Ayat',
	},
	{
		id: '66',
		city_name_en: 'Al-Bawaiti',
	},
	{
		id: '67',
		city_name_en: 'ManshiyetAl Qanater',
	},
	{
		id: '68',
		city_name_en: 'Oaseem',
	},
	{
		id: '69',
		city_name_en: 'Kerdasa',
	},
	{
		id: '70',
		city_name_en: 'Abu Nomros',
	},
	{
		id: '71',
		city_name_en: 'Kafr Ghati',
	},
	{
		id: '72',
		city_name_en: 'Manshiyet Al Bakari',
	},
	{
		id: '73',
		city_name_en: 'Dokki',
	},
	{
		id: '74',
		city_name_en: 'Agouza',
	},
	{
		id: '75',
		city_name_en: 'Haram',
	},
	{
		id: '76',
		city_name_en: 'Warraq',
	},
	{
		id: '77',
		city_name_en: 'Imbaba',
	},
	{
		id: '78',
		city_name_en: 'Boulaq Dakrour',
	},
	{
		id: '79',
		city_name_en: 'Al Wahat Al Baharia',
	},
	{
		id: '80',
		city_name_en: 'Omraneya',
	},
	{
		id: '81',
		city_name_en: 'Moneeb',
	},
	{
		id: '82',
		city_name_en: 'Bin Alsarayat',
	},
	{
		id: '83',
		city_name_en: 'Kit Kat',
	},
	{
		id: '84',
		city_name_en: 'Mohandessin',
	},
	{
		id: '85',
		city_name_en: 'Faisal',
	},
	{
		id: '86',
		city_name_en: 'Abu Rawash',
	},
	{
		id: '87',
		city_name_en: 'Hadayek Alahram',
	},
	{
		id: '88',
		city_name_en: 'Haraneya',
	},
	{
		id: '89',
		city_name_en: 'Hadayek October',
	},
	{
		id: '90',
		city_name_en: 'Saft Allaban',
	},
	{
		id: '91',
		city_name_en: 'Smart Village',
	},
	{
		id: '92',
		city_name_en: 'Ard Ellwaa',
	},
];
var Alexandria_cities = [
	{
		id: '93',
		city_name_en: 'Abu Qir',
	},
	{
		id: '94',
		city_name_en: 'Al Ibrahimeyah',
	},
	{
		id: '95',
		city_name_en: 'Azarita',
	},
	{
		id: '96',
		city_name_en: 'Anfoushi',
	},
	{
		id: '97',
		city_name_en: 'Dekheila',
	},
	{
		id: '98',
		city_name_en: 'El Soyof',
	},
	{
		id: '99',
		city_name_en: 'Ameria',
	},
	{
		id: '100',
		city_name_en: 'El Labban',
	},
	{
		id: '101',
		city_name_en: 'Al Mafrouza',
	},
	{
		id: '102',
		city_name_en: 'El Montaza',
	},
	{
		id: '103',
		city_name_en: 'Mansheya',
	},
	{
		id: '104',
		city_name_en: 'Naseria',
	},
	{
		id: '105',
		city_name_en: 'Ambrozo',
	},
	{
		id: '106',
		city_name_en: 'Bab Sharq',
	},
	{
		id: '107',
		city_name_en: 'Bourj Alarab',
	},
	{
		id: '108',
		city_name_en: 'Stanley',
	},
	{
		id: '109',
		city_name_en: 'Smouha',
	},
	{
		id: '110',
		city_name_en: 'Sidi Bishr',
	},
	{
		id: '111',
		city_name_en: 'Shads',
	},
	{
		id: '112',
		city_name_en: 'Gheet Alenab',
	},
	{
		id: '113',
		city_name_en: 'Fleming',
	},
	{
		id: '114',
		city_name_en: 'Victoria',
	},
	{
		id: '115',
		city_name_en: 'Camp Shizar',
	},
	{
		id: '116',
		city_name_en: 'Karmooz',
	},
	{
		id: '117',
		city_name_en: 'Mahta Alraml',
	},
	{
		id: '118',
		city_name_en: 'Mina El-Basal',
	},
	{
		id: '119',
		city_name_en: 'Asafra',
	},
	{
		id: '120',
		city_name_en: 'Agamy',
	},
	{
		id: '121',
		city_name_en: 'Bakos',
	},
	{
		id: '122',
		city_name_en: 'Boulkly',
	},
	{
		id: '123',
		city_name_en: 'Cleopatra',
	},
	{
		id: '124',
		city_name_en: 'Glim',
	},
	{
		id: '125',
		city_name_en: 'Al Mamurah',
	},
	{
		id: '126',
		city_name_en: 'Al Mandara',
	},
	{
		id: '127',
		city_name_en: 'Moharam Bek',
	},
	{
		id: '128',
		city_name_en: 'Elshatby',
	},
	{
		id: '129',
		city_name_en: 'Sidi Gaber',
	},
	{
		id: '130',
		city_name_en: 'North Coast/sahel',
	},
	{
		id: '131',
		city_name_en: 'Alhadra',
	},
	{
		id: '132',
		city_name_en: 'Alattarin',
	},
	{
		id: '133',
		city_name_en: 'Sidi Kerir',
	},
	{
		id: '134',
		city_name_en: 'Elgomrok',
	},
	{
		id: '135',
		city_name_en: 'Al Max',
	},
	{
		id: '136',
		city_name_en: 'Marina',
	},
];
var Dakahlia_cities = [
	{
		id: '137',
		city_name_en: 'Mansoura',
	},
	{
		id: '138',
		city_name_en: 'Talkha',
	},
	{
		id: '139',
		city_name_en: 'Mitt Ghamr',
	},
	{
		id: '140',
		city_name_en: 'Dekernes',
	},
	{
		id: '141',
		city_name_en: 'Aga',
	},
	{
		id: '142',
		city_name_en: 'Menia El Nasr',
	},
	{
		id: '143',
		city_name_en: 'Sinbillawin',
	},
	{
		id: '144',
		city_name_en: 'El Kurdi',
	},
	{
		id: '145',
		city_name_en: 'Bani Ubaid',
	},
	{
		id: '146',
		city_name_en: 'Al Manzala',
	},
	{
		id: '147',
		city_name_en: "tami al'amdid",
	},
	{
		id: '148',
		city_name_en: 'aljamalia',
	},
	{
		id: '149',
		city_name_en: 'Sherbin',
	},
	{
		id: '150',
		city_name_en: 'Mataria',
	},
	{
		id: '151',
		city_name_en: 'Belqas',
	},
	{
		id: '152',
		city_name_en: 'Meet Salsil',
	},
	{
		id: '153',
		city_name_en: 'Gamasa',
	},
	{
		id: '154',
		city_name_en: 'Mahalat Damana',
	},
	{
		id: '155',
		city_name_en: 'Nabroh',
	},
];
var RedSea_cities = [
	{
		id: '156',
		city_name_en: 'Hurghada',
	},
	{
		id: '157',
		city_name_en: 'Ras Ghareb',
	},
	{
		id: '158',
		city_name_en: 'Safaga',
	},
	{
		id: '159',
		city_name_en: 'El Qusiar',
	},
	{
		id: '160',
		city_name_en: 'Marsa Alam',
	},
	{
		id: '161',
		governorate_id: '5',
		city_name_ar: 'الشلاتين',
		city_name_en: 'Shalatin',
	},
	{
		id: '162',
		city_name_en: 'Halaib',
	},
	{
		id: '163',
		city_name_en: 'Aldahar',
	},
];
var Beheira_cities = [
	{
		id: '164',
		city_name_en: 'Damanhour',
	},
	{
		id: '165',
		city_name_en: 'Kafr El Dawar',
	},
	{
		id: '166',
		city_name_en: 'Rashid',
	},
	{
		id: '167',
		city_name_en: 'Edco',
	},
	{
		id: '168',
		city_name_en: 'Abu al-Matamir',
	},
	{
		id: '169',
		city_name_en: 'Abu Homs',
	},
	{
		id: '170',
		city_name_en: 'Delengat',
	},
	{
		id: '171',
		city_name_en: 'Mahmoudiyah',
	},
	{
		id: '172',
		city_name_en: 'Rahmaniyah',
	},
	{
		id: '173',
		city_name_en: 'Itai Baroud',
	},
	{
		id: '174',
		city_name_en: 'Housh Eissa',
	},
	{
		id: '175',
		city_name_en: 'Shubrakhit',
	},
	{
		id: '176',
		city_name_en: 'Kom Hamada',
	},
	{
		id: '177',
		city_name_en: 'Badr',
	},
	{
		id: '178',
		city_name_en: 'Wadi Natrun',
	},
	{
		id: '179',
		city_name_en: 'New Nubaria',
	},
	{
		id: '180',
		city_name_en: 'Alnoubareya',
	},
];
var Fayoum_cities = [
	{
		id: '181',
		city_name_en: 'Fayoum',
	},
	{
		id: '182',
		city_name_en: 'Fayoum El Gedida',
	},
	{
		id: '183',
		city_name_en: 'Tamiya',
	},
	{
		id: '184',
		city_name_en: 'Snores',
	},
	{
		id: '185',
		city_name_en: 'Etsa',
	},
	{
		id: '186',
		city_name_en: 'Epschway',
	},
	{
		id: '187',
		city_name_en: 'Yusuf El Sediaq',
	},
	{
		id: '188',
		city_name_en: 'Hadqa',
	},
	{
		id: '189',
		city_name_en: 'Atsa',
	},
	{
		id: '190',
		city_name_en: 'Algamaa',
	},
	{
		id: '191',
		city_name_en: 'Sayala',
	},
];
var Gharbiya_cities = [
	{
		id: '192',
		city_name_en: 'Tanta',
	},
	{
		id: '193',
		city_name_en: 'Al Mahalla Al Kobra',
	},
	{
		id: '194',
		city_name_en: 'Kafr El Zayat',
	},
	{
		id: '195',
		city_name_en: 'Zefta',
	},
	{
		id: '196',
		city_name_en: 'El Santa',
	},
	{
		id: '197',
		city_name_en: 'Qutour',
	},
	{
		id: '198',
		city_name_en: 'Basion',
	},
	{
		id: '199',
		city_name_en: 'Samannoud',
	},
];
var Ismailia_cities = [
	{
		id: '200',
		city_name_en: 'Ismailia',
	},
	{
		id: '201',
		city_name_en: 'Fayed',
	},
	{
		id: '202',
		city_name_en: 'Qantara Sharq',
	},
	{
		id: '203',
		city_name_en: 'Qantara Gharb',
	},
	{
		id: '204',
		city_name_en: 'El Tal El Kabier',
	},
	{
		id: '205',
		city_name_en: 'Abu Sawir',
	},
	{
		id: '206',
		city_name_en: 'Kasasien El Gedida',
	},
	{
		id: '207',
		city_name_en: 'Nefesha',
	},
	{
		id: '208',
		city_name_en: 'Sheikh Zayed',
	},
];
var Menofia_cities = [
	{
		id: '209',
		city_name_en: 'Shbeen El Koom',
	},
	{
		id: '210',
		city_name_en: 'Sadat City',
	},
	{
		id: '211',
		city_name_en: 'Menouf',
	},
	{
		id: '212',
		city_name_en: 'Sars El-Layan',
	},
	{
		id: '213',
		city_name_en: 'Ashmon',
	},
	{
		id: '214',
		city_name_en: 'Al Bagor',
	},
	{
		id: '215',
		city_name_en: 'Quesna',
	},
	{
		id: '216',
		city_name_en: 'Berkat El Saba',
	},
	{
		id: '217',
		city_name_en: 'Tala',
	},
	{
		id: '218',
		city_name_en: 'Al Shohada',
	},
];
var Minya_cities = [
	{
		id: '219',
		city_name_en: 'Minya',
	},
	{
		id: '220',
		city_name_en: 'Minya El Gedida',
	},
	{
		id: '221',
		city_name_en: 'El Adwa',
	},
	{
		id: '222',
		city_name_en: 'Magagha',
	},
	{
		id: '223',
		city_name_en: 'Bani Mazar',
	},
	{
		id: '224',
		city_name_en: 'Mattay',
	},
	{
		id: '225',
		city_name_en: 'Samalut',
	},
	{
		id: '226',
		city_name_en: 'Madinat El Fekria',
	},
	{
		id: '227',
		city_name_en: 'Meloy',
	},
	{
		id: '228',
		city_name_en: 'Deir Mawas',
	},
	{
		id: '229',
		city_name_en: 'Abu Qurqas',
	},
	{
		id: '230',
		city_name_en: 'Ard Sultan',
	},
];
var Qaliubiya_cities = [
	{
		id: '231',
		city_name_en: 'Banha',
	},
	{
		id: '232',
		city_name_en: 'Qalyub',
	},
	{
		id: '233',
		city_name_en: 'Shubra Al Khaimah',
	},
	{
		id: '234',
		city_name_en: 'Al Qanater Charity',
	},
	{
		id: '235',
		city_name_en: 'Khanka',
	},
	{
		id: '236',
		city_name_en: 'Kafr Shukr',
	},
	{
		id: '237',
		city_name_en: 'Tukh',
	},
	{
		id: '238',
		city_name_en: 'Qaha',
	},
	{
		id: '239',
		city_name_en: 'Obour',
	},
	{
		id: '240',
		city_name_en: 'Khosous',
	},
	{
		id: '241',
		city_name_en: 'Shibin Al Qanater',
	},
	{
		id: '242',
		city_name_en: 'Mostorod',
	},
];
var NewValley_cities = [
	{
		id: '243',
		city_name_en: 'El Kharga',
	},
	{
		id: '244',
		city_name_en: 'Paris',
	},
	{
		id: '245',
		city_name_en: 'Mout',
	},
	{
		id: '246',
		city_name_en: 'Farafra',
	},
	{
		id: '247',
		city_name_en: 'Balat',
	},
	{
		id: '248',
		city_name_en: 'Dakhla',
	},
];
var Suez_cities = [
	{
		id: '249',
		city_name_en: 'Suez',
	},
	{
		id: '250',
		city_name_en: 'Alganayen',
	},
	{
		id: '251',
		city_name_en: 'Ataqah',
	},
	{
		id: '252',
		city_name_en: 'Ain Sokhna',
	},
	{
		id: '253',
		city_name_en: 'Faysal',
	},
];
var Aswan_cities = [
	{
		id: '254',
		city_name_en: 'Aswan',
	},
	{
		id: '255',
		city_name_en: 'Aswan El Gedida',
	},
	{
		id: '256',
		city_name_en: 'Drau',
	},
	{
		id: '257',
		city_name_en: 'Kom Ombo',
	},
	{
		id: '258',
		city_name_en: 'Nasr Al Nuba',
	},
	{
		id: '259',
		city_name_en: 'Kalabsha',
	},
	{
		id: '260',
		city_name_en: 'Edfu',
	},
	{
		id: '261',
		city_name_en: 'Al-Radisiyah',
	},
	{
		id: '262',
		city_name_en: 'Al Basilia',
	},
	{
		id: '263',
		city_name_en: 'Al Sibaeia',
	},
	{
		id: '264',
		city_name_en: 'Abo Simbl Al Siyahia',
	},
	{
		id: '265',
		city_name_en: 'Marsa Alam',
	},
];
var Assiut_cities = [
	{
		id: '266',
		city_name_en: 'Assiut',
	},
	{
		id: '267',
		city_name_en: 'Assiut El Gedida',
	},
	{
		id: '268',
		city_name_en: 'Dayrout',
	},
	{
		id: '269',
		city_name_en: 'Manfalut',
	},
	{
		id: '270',
		city_name_en: 'Qusiya',
	},
	{
		id: '271',
		city_name_en: 'Abnoub',
	},
	{
		id: '272',
		city_name_en: 'Abu Tig',
	},
	{
		id: '273',
		city_name_en: 'El Ghanaim',
	},
	{
		id: '274',
		city_name_en: 'Sahel Selim',
	},
	{
		id: '275',
		city_name_en: 'El Badari',
	},
	{
		id: '276',
		city_name_en: 'Sidfa',
	},
];
var BeniSuef_cities = [
	{
		id: '277',
		city_name_en: 'Bani Sweif',
	},
	{
		id: '278',
		city_name_en: 'Beni Suef El Gedida',
	},
	{
		id: '279',
		city_name_en: 'Al Wasta',
	},
	{
		id: '280',
		city_name_en: 'Naser',
	},
	{
		id: '281',
		city_name_en: 'Ehnasia',
	},
	{
		id: '282',
		city_name_en: 'beba',
	},
	{
		id: '283',
		city_name_en: 'Fashn',
	},
	{
		id: '284',
		city_name_en: 'Somasta',
	},
	{
		id: '285',
		city_name_en: 'Alabbaseri',
	},
	{
		id: '286',
		city_name_en: 'Mokbel',
	},
];
var PortSaid_cities = [
	{
		id: '287',
		city_name_en: 'PorSaid',
	},
	{
		id: '288',
		city_name_en: 'Port Fouad',
	},
	{
		id: '289',
		city_name_en: 'Alarab',
	},
	{
		id: '290',
		city_name_en: 'Zohour',
	},
	{
		id: '291',
		city_name_en: 'Alsharq',
	},
	{
		id: '292',
		city_name_en: 'Aldawahi',
	},
	{
		id: '293',
		city_name_en: 'Almanakh',
	},
	{
		id: '294',
		city_name_en: 'Mubarak',
	},
];
var Damietta_cities = [
	{
		id: '295',
		city_name_en: 'Damietta',
	},
	{
		id: '296',
		city_name_en: 'New Damietta',
	},
	{
		id: '297',
		city_name_en: 'Ras El Bar',
	},
	{
		id: '298',
		city_name_en: 'Faraskour',
	},
	{
		id: '299',
		city_name_en: 'Zarqa',
	},
	{
		id: '300',
		city_name_en: 'alsaru',
	},
	{
		id: '301',
		city_name_en: 'alruwda',
	},
	{
		id: '302',
		city_name_en: 'Kafr El-Batikh',
	},
	{
		id: '303',
		city_name_en: 'Azbet Al Burg',
	},
	{
		id: '304',
		city_name_en: 'Meet Abou Ghalib',
	},
	{
		id: '305',
		city_name_en: 'Kafr Saad',
	},
];
var Sharkia_cities = [
	{
		id: '306',
		city_name_en: 'Zagazig',
	},
	{
		id: '307',
		city_name_en: 'Al Ashr Men Ramadan',
	},
	{
		id: '308',
		city_name_en: 'Minya Al Qamh',
	},
	{
		id: '309',
		city_name_en: 'Belbeis',
	},
	{
		id: '310',
		city_name_en: 'Mashtoul El Souq',
	},
	{
		id: '311',
		city_name_en: 'Qenaiat',
	},
	{
		id: '312',
		city_name_en: 'Abu Hammad',
	},
	{
		id: '313',
		city_name_en: 'El Qurain',
	},
	{
		id: '314',
		city_name_en: 'Hehia',
	},
	{
		id: '315',
		city_name_en: 'Abu Kabir',
	},
	{
		id: '316',
		city_name_en: 'Faccus',
	},
	{
		id: '317',
		city_name_en: 'El Salihia El Gedida',
	},
	{
		id: '318',
		city_name_en: 'Al Ibrahimiyah',
	},
	{
		id: '319',
		city_name_en: 'Deirb Negm',
	},
	{
		id: '320',
		city_name_en: 'Kafr Saqr',
	},
	{
		id: '321',
		city_name_en: 'Awlad Saqr',
	},
	{
		id: '322',
		city_name_en: 'Husseiniya',
	},
	{
		id: '323',
		city_name_en: 'san alhajar alqablia',
	},
	{
		id: '324',
		city_name_en: 'Manshayat Abu Omar',
	},
];
var SouthSinai_cities = [
	{
		id: '325',
		city_name_en: 'Al Toor',
	},
	{
		id: '326',
		city_name_en: 'Sharm El-Shaikh',
	},
	{
		id: '327',
		city_name_en: 'Dahab',
	},
	{
		id: '328',
		city_name_en: 'Nuweiba',
	},
	{
		id: '329',
		city_name_en: 'Taba',
	},
	{
		id: '330',
		city_name_en: 'Saint Catherine',
	},
	{
		id: '331',
		city_name_en: 'Abu Redis',
	},
	{
		id: '332',
		city_name_en: 'Abu Zenaima',
	},
	{
		id: '333',
		city_name_en: 'Ras Sidr',
	},
];
var KafrAlsheikh_cities = [
	{
		id: '334',
		city_name_en: 'Kafr El Sheikh',
	},
	{
		id: '335',
		city_name_en: 'Kafr El Sheikh Downtown',
	},
	{
		id: '336',
		city_name_en: 'Desouq',
	},
	{
		id: '337',
		city_name_en: 'Fooh',
	},
	{
		id: '338',
		city_name_en: 'Metobas',
	},
	{
		id: '339',
		city_name_en: 'Burg Al Burullus',
	},
	{
		id: '340',
		city_name_en: 'Baltim',
	},
	{
		id: '341',
		city_name_en: 'Masief Baltim',
	},
	{
		id: '342',
		city_name_en: 'Hamol',
	},
	{
		id: '343',
		city_name_en: 'Bella',
	},
	{
		id: '344',
		city_name_en: 'Riyadh',
	},
	{
		id: '345',
		city_name_en: 'Sidi Salm',
	},
	{
		id: '346',
		city_name_en: 'Qellen',
	},
	{
		id: '347',
		city_name_en: 'Sidi Ghazi',
	},
];
var Matrouh_cities = [
	{
		id: '348',
		city_name_en: 'Marsa Matrouh',
	},
	{
		id: '349',
		city_name_en: 'El Hamam',
	},
	{
		id: '350',
		city_name_en: 'Alamein',
	},
	{
		id: '351',
		city_name_en: 'Dabaa',
	},
	{
		id: '352',
		city_name_en: 'Al-Nagila',
	},
	{
		id: '353',
		city_name_en: 'Sidi Brani',
	},
	{
		id: '354',
		city_name_en: 'Salloum',
	},
	{
		id: '355',
		city_name_en: 'Siwa',
	},
	{
		id: '356',
		city_name_en: 'Marina',
	},
	{
		id: '357',
		city_name_en: 'North Coast',
	},
];
var Luxor_cities = [
	{
		id: '358',
		city_name_en: 'Luxor',
	},
	{
		id: '359',
		city_name_en: 'New Luxor',
	},
	{
		id: '360',
		city_name_en: 'Esna',
	},
	{
		id: '361',
		city_name_en: 'New Tiba',
	},
	{
		id: '362',
		city_name_en: 'Al ziynia',
	},
	{
		id: '363',
		city_name_en: 'Al Bayadieh',
	},
	{
		id: '364',
		city_name_en: 'Al Qarna',
	},
	{
		id: '365',
		city_name_en: 'Armant',
	},
	{
		id: '366',
		city_name_en: 'Al Tud',
	},
];
var Qena_cities = [
	{
		id: '367',
		city_name_en: 'Qena',
	},
	{
		id: '368',
		city_name_en: 'New Qena',
	},
	{
		id: '369',
		city_name_en: 'Abu Tesht',
	},
	{
		id: '370',
		city_name_en: 'Nag Hammadi',
	},
	{
		id: '371',
		city_name_en: 'Deshna',
	},
	{
		id: '372',
		city_name_en: 'Alwaqf',
	},
	{
		id: '373',
		city_name_en: 'Qaft',
	},
	{
		id: '374',
		city_name_en: 'Naqada',
	},
	{
		id: '375',
		city_name_en: 'Farshout',
	},
	{
		id: '376',
		city_name_en: 'Quos',
	},
];
var NorthSinai_cities = [
	{
		id: '377',
		city_name_en: 'Arish',
	},
	{
		id: '378',
		city_name_en: 'Sheikh Zowaid',
	},
	{
		id: '379',
		city_name_en: 'Nakhl',
	},
	{
		id: '380',
		governorate_id: '26',
		city_name_ar: 'رفح',
		city_name_en: 'Rafah',
	},
	{
		id: '381',
		city_name_en: 'Bir al-Abed',
	},
	{
		id: '382',
		city_name_en: 'Al Hasana',
	},
];
var Sohag_cities = [
	{
		id: '383',
		city_name_en: 'Sohag',
	},
	{
		id: '384',
		city_name_en: 'Sohag El Gedida',
	},
	{
		id: '385',
		city_name_en: 'Akhmeem',
	},
	{
		id: '386',
		city_name_en: 'Akhmim El Gedida',
	},
	{
		id: '387',
		city_name_en: 'Albalina',
	},
	{
		id: '388',
		city_name_en: 'El Maragha',
	},
	{
		id: '389',
		city_name_en: "almunsha'a",
	},
	{
		id: '390',
		city_name_en: 'Dar AISalaam',
	},
	{
		id: '391',
		city_name_en: 'Gerga',
	},
	{
		id: '392',
		city_name_en: 'Jahina Al Gharbia',
	},
	{
		id: '393',
		city_name_en: 'Saqilatuh',
	},
	{
		id: '394',
		city_name_en: 'Tama',
	},
	{
		id: '395',
		city_name_en: 'Tahta',
	},
	{
		id: '396',
		city_name_en: 'Alkawthar',
	},
];

var htmlcontent = "<option value='' hidden>Select Governate</option>";
for (var i = 0; i < governerate.length; i++) {
	htmlcontent =
		htmlcontent +
		"<option value='" +
		governerate[i].id +
		"'>" +
		governerate[i].governorate_name_en +
		'</option>';
}

$('#inputState').html(htmlcontent);

$('#inputState').change(function () {
	var StateSelected = $(this).val();
	var optionsList;
	var htmlString = '';
	switch (StateSelected) {
		case '1':
			optionsList = cairo_cities;
			break;
		case '2':
			optionsList = Giza_cities;
			break;
		case '3':
			optionsList = Alexandria_cities;
			break;
		case '4':
			optionsList = Dakahlia_cities;
			break;
		case '5':
			optionsList = RedSea_cities;
			break;
		case '6':
			optionsList = Beheira_cities;
			break;
		case '7':
			optionsList = Fayoum_cities;
			break;
		case '8':
			optionsList = Gharbiya_cities;
			break;
		case '9':
			optionsList = Ismailia_cities;
			break;
		case '10':
			optionsList = Menofia_cities;
			break;
		case '11':
			optionsList = Minya_cities;
			break;
		case '12':
			optionsList = Qaliubiya_cities;
			break;
		case '13':
			optionsList = NewValley_cities;
			break;
		case '14':
			optionsList = Suez_cities;
			break;
		case '15':
			optionsList = Aswan_cities;
			break;
		case '16':
			optionsList = Assiut_cities;
			break;
		case '17':
			optionsList = BeniSuef_cities;
			break;
		case '18':
			optionsList = PortSaid_cities;
			break;
		case '19':
			optionsList = Damietta_cities;
			break;
		case '20':
			optionsList = Sharkia_cities;
			break;
		case '21':
			optionsList = SouthSinai_cities;
			break;
		case '22':
			optionsList = KafrAlsheikh_cities;
			break;
		case '23':
			optionsList = Matrouh_cities;
			break;
		case '24':
			optionsList = Luxor_cities;
			break;
		case '25':
			optionsList = Qena_cities;
			break;
		case '26':
			optionsList = NorthSinai_cities;
			break;
		case '27':
			optionsList = Sohag_cities;
			break;
	}

	for (var i = 0; i < optionsList.length; i++) {
		htmlString =
			htmlString +
			"<option value='" +
			optionsList[i].id +
			"'>" +
			optionsList[i].city_name_en +
			'</option>';
	}
	$('#inputCity').html(htmlString);
});
