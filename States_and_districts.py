import random

states = ["Andhra Pradesh", "Arunachal Pradesh ", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana",
          "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh",
          "Maharashtra",
          "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu",
          "Telangana",
          "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal", "Andaman and Nicobar Islands", "Chandigarh",
          "Dadra and Nagar Haveli", "Daman and Diu", "Lakshadweep", "National Capital Territory of Delhi",
          "Puducherry"]
# link = "https://www.delhimetrotimes.in/arunachal-pradesh/list-of-district-in-arunachal-pradesh.html"
district_1 = ["Ananthapur", "Chittoor", "Cuddapah", "East Godavari", "Guntur", "Krishna", "Kurnool", "Nellore",
              "Prakasam", "Srikakulam",
              "Visakhapatnam", "Vizianagaram", "West Godavari"]
district_2 = ["Changlang", "Dibang Valley", "East Kameng", "East Siang", "Kurung Kumey", "Lohit", "Lower Dibang Valley",
              "Lower Subansiri", "Papum Pare", "Tawang", "Tirap", "Upper Siang", "Upper Subansiri", "West Kameng",
              "West Siang"]
district_3 = ["Barpeta", "Bongaigaon", "Cachar", "Darrang", "Dhemaji", "Dhubri", "Dibrugarh", "Goalpara", "Golaghat",
              "Hailakandi", "Jorhat", "Kamrup", "Karbi Anglong",
              "Karimganj", "Kokrajhar", "Lakhimpur", "Marigaon", "Nagaon", "Nalbari", "North Cachar Hills", "Sibsagar",
              "Sonitpur", "Tinsukia"]
district_4 = ["Araria", "Arwal", "Aurangabad(BH)", "Banka", "Begusarai", "Bhagalpur", "Bhojpur", "Buxar", "Darbhanga",
              "East Champaran", "Gaya", "Gopalganj", "Jamui",
              "Jehanabad", "Kaimur(Bhabua)", "Katihar", "Khagaria", "Kishanganj", "Lakhisarai", "Madhepura", "Munger",
              "Muzaffarpur", "Nalanda", "Nawada,"    "Patna", "Purnia", "Rohtas",
              "Saharsa", "Samastipur", "Saran", "Sheikhpura", "Sheohar", "Sitamarhi", "Siwan", "Supaul", "Vaishali",
              "West Champaran"]
district_5 = ["Bastar", "Bijapur(CGH)", "Bilaspur(CGH)", "Dantewada", "Dhamtari", "Durg", "Gariaband",
              "Janjgir - champa", "Jashpur",
              "Kanker", "Kawardha", "Korba", "Koriya", "Mahasamund",
              "Narayanpur", "Raigarh", "Raipur", "Rajnandgaon", "Surguja"]
district_6 = ["North Goa", "South Goa"]
district_7 = ["Ahmedabad", "Amreli", "Anand", "Banaskantha", "Bharuch", "Bhavnagar", "Dahod", "Gandhi Nagar",
              "Jamnagar", "Junagadh", "Kachchh", "Kheda", "Mahesana", "Narmada",
              'Navsari', 'Panch Mahals', 'Patan', 'Porbandar', 'Rajkot', "Sabarkantha", "Surat", "Surendra Nagar",
              "Tapi", "The Dangs", "Vadodara", "Valsad"]
district_8 = ['Ambala', 'Bhiwani', 'Faridabad', 'Fatehabad', 'Gurgaon', 'Hisar', 'Jhajjar', 'Jind',
              'Kaithal', "Karnal", "Kurukshetra", "Mahendragarh,""Panchkula", "Panipat",
              'Rewari', 'Rohtak', 'Sirsa', 'Sonipat', 'Yamuna Nagar']
district_9 = ['Bilaspur (HP)', 'Chamba', 'Hamirpur(HP)', 'Kangra', 'Kinnaur', 'Kullu', 'Lahul & Spiti', 'Mandi',
              'Shimla', 'Sirmaur', 'Solan', 'Una']
district_10 = ['Ananthnag', 'Bandipur', 'Baramulla', 'Budgam', 'Doda', 'Jammu', 'Kargil', 'Kathua', 'Kulgam', 'Kupwara',
               'Leh', 'Poonch',
               'Pulwama', 'Rajauri', 'Reasi', 'Shopian',
               'Srinagar', 'Udhampur']
district_11 = ['Bokaro', 'Chatra', 'Deoghar', 'Dhanbad', 'Dumka', 'East Singhbhum', 'Garhwa', 'Giridh', 'Godda',
               'Gumla', 'Hazaribag',
               'Jamtara', 'Khunti',
               'Koderma', 'Latehar', 'Lohardaga', 'Pakur', 'Palamau', 'Ramgarh', 'Ranchi', 'Sahibganj',
               'Seraikela - kharsawan',
               'Simdega',
               'West Singhbhum']
district_12 = ['Bagalkot', 'Bangalore', 'Bangalore Rural', 'Belgaum', 'Bellary', 'Bidar', 'Bijapur(KAR)',
               'Chamrajnagar',
               'Chickmagalur',
               'Chikkaballapur', 'Chitradurga',
               'Dakshina Kannada', 'Davangere', 'Dharwad', 'Gadag', 'Gulbarga', 'Hassan', 'Haveri', 'Kodagu', 'Kolar',
               'Koppal', 'Mandya',
               'Mysore', 'Raichur', 'Ramanagar', 'Shimoga',
               'Tumkur', 'Udupi', 'Uttara Kannada', 'Yadgir']
district_13 = ['Alappuzha', 'Ernakulam', 'Idukki', 'Kannur', 'Kasargod', ' Kollam', 'Kottayam', 'Kozhikode',
               'Malappuram', 'Palakkad',
               'Pathanamthitta', 'Thiruvananthapuram', 'Thrissur', 'Wayanad']
district_14 = ['Alirajpur', 'Anuppur', 'Ashok Nagar', ' Balaghat', 'Barwani', 'Betul', 'Bhind', 'Bhopal', 'Burhanpur',
               'Chhatarpur',
               'Chhindwara', 'Damoh',
               'Datia', 'Dewas', 'Dhar', 'Dindori', 'East Nimar', 'Guna', 'Gwalior', 'Harda', 'Hoshangabad', 'Indore',
               'Jabalpur',
               'Jhabua', 'Katni', 'Khandwa', 'Khargone', 'Mandla', 'Mandsaur', 'Morena', 'Narsinghpur', 'Neemuch',
               'Panna', 'Raisen', 'Rajgarh',
               'Ratlam',
               'Rewa', 'Sagar', 'Satna', 'Sehore', 'Seoni', 'Shahdol', 'Shajapur', 'Sheopur', 'Shivpuri', 'Sidhi',
               'Singrauli', 'Tikamgarh',
               'Ujjain', 'Umaria', 'Vidisha',
               'West Nimar']
district_15 = ['Ahmed Nagar', 'Akola', 'Amravati', 'Aurangabad', 'Beed', 'Bhandara', 'Buldhana', 'Chandrapur', 'Dhule',
               'Gadchiroli',
               'Gondia', 'Hingoli',
               'Jalgaon', 'Jalna', 'Kolhapur', 'Latur', 'Mumbai', 'Nagpur', 'Nanded', 'Nandurbar', 'Nashik',
               'Osmanabad', 'Parbhani', 'Pune',
               'Raigarh(MH)', 'Ratnagiri', 'Sangli', 'Satara', 'Sindhudurg', 'Solapur', 'Thane', 'Wardha', 'Washim',
               'Yavatmal']
district_16 = ['Bishnupur', 'Chandel', 'Churachandpur', 'Imphal East', 'Imphal West', 'Senapati', 'Tamenglong',
               'Thoubal',
               'Ukhrul']
district_17 = ['East Garo Hills', 'East Khasi Hills', 'Jaintia Hills', 'Ri Bhoi', 'South Garo Hills', 'West Garo Hills',
               'West Khasi Hills']
district_18 = ['Aizawl', 'Champhai', 'Kolasib', 'Lawngtlai', 'Lunglei', 'Mammit', 'Saiha', 'Serchhip']
district_19 = ['Dimapur', 'Kiphire', 'Kohima', 'Longleng', 'Mokokchung', 'Mon', 'Peren', 'Phek',
               'Tuensang', 'Wokha', 'Zunhebotto']
district_20 = ['Angul', 'Balangir', 'Baleswar', 'Bargarh', 'Bhadrak', 'Boudh', 'Cuttack', 'Debagarh', 'Dhenkanal',
               'Gajapati', 'Ganjam',
               'Jagatsinghapur', 'Jajapur', 'Jharsuguda', 'Kalahandi', 'Kandhamal', 'Kendraparan', 'Kendujhar',
               'Khorda', 'Koraput',
               'Malkangiri', 'Mayurbhanj', 'Nabarangapur', 'Nayagarh', 'Nuapada', 'Puri', 'Rayagada', 'Sambalpur',
               'Sonapur', 'Sundergarh']
district_21 = ['Amritsar', 'Barnala', 'Bathinda', 'Faridkot', 'Fatehgarh Sahib', 'Fazilka', 'Firozpur', 'Gurdaspur',
               'Hoshiarpur',
               'Jalandhar', 'Kapurthala', 'Ludhiana', 'Mansa', 'Moga', 'Mohali', 'Muktsar', 'Nawanshahr', 'Pathankot',
               'Patiala', 'Ropar', 'Rupnagar', 'Sangrur', 'Tarn Taran']
district_22 = ['Ajmer', 'Alwar', 'Banswara', 'Baran', 'Barmer', 'Bharatpur', 'Bhilwara', 'Bikaner', 'Bundi',
               'Chittorgarh', 'Churu', 'Dausa',
               'Dholpur', 'Dungarpur', 'Ganganagar', 'Hanumangarh', 'Jaipur', 'Jaisalmer', 'Jalor', 'Jhalawar',
               'Jhujhunu', 'Jodhpur',
               'Karauli', 'Kota', 'Nagaur', 'Pali', 'Rajsamand', 'Sawai Madhopur', 'Sikar', 'Sirohi', 'Tonk', 'Udaipur']
district_23 = ["East Sikkim", "North Sikkim", "South Sikkim", "West Sikkim"]
district_24 = ["Ariyalur", "Chengalpattu", "Chennai", "Coimbatore", "Cuddalore", "Dharmapuri", "Dindigul", "Erode",
               "Kallakurichi", "Kanchipuram", "Kanyakumari", "Karur", "Krishnagiri", "Madurai", "Nagapattinam",
               "Namakkal",
               "Nilgiris", "Perambalur", "Pudukkottai", "Ramanathapuram", "Ranipet", "Salem", "Sivaganga", "Tenkasi",
               "Thanjavur", "Theni", "Thoothukudi (Tuticorin)", "Tiruchirappalli", "Tirunelveli", "Tirupathur",
               "Tiruppur",
               "Tiruvallur", "Tiruvannamalai", "Tiruvarur", "Vellore", "Viluppuram", "Virudhunagar"]
district_25 = ["Adilabad", "Bhadradri Kothagudem", "Hyderabad", "Jagtial", "Jangaon", "Jayashankar Bhoopalpally",
               "Jogulamba Gadwal", "Kamareddy", "Karimnagar", "Khammam", "Komaram Bheem Asifabad", "Mahabubabad",
               "Mahabubnagar", "Mancherial", "Medak", "Medchal", "Nagarkurnool", "Nalgonda", "Nirmal", "Nizamabad",
               "Peddapalli", "Rajanna Sircilla", "Rangareddy", "Sangareddy", "Siddipet", "Suryapet", "Vikarabad",
               "Wanaparthy", "Warangal (Rural)", "Warangal (Urban)", "Yadadri Bhuvanagiri"]
district_26 = ["Dhalai", "Gomati", "Khowai", "North Tripura", "Sepahijala", "South Tripura", "Unakoti", "West Tripura"]
district_27 = ["Agra", "Aligarh", "Allahabad", "Ambedkar Nagar", "Amethi (Chatrapati Sahuji Mahraj Nagar)",
               "Amroha (J.P. Nagar)", "Auraiya", "Azamgarh", "Baghpat", "Bahraich", "Ballia", "Balrampur",
               "Banda", "Barabanki", "Bareilly", "Basti", "Bhadohi", "Bijnor", "Budaun", "Bulandshahr",
               "Chandauli", "Chitrakoot", "Deoria", "Etah", "Etawah", "Faizabad", "Farrukhabad", "Fatehpur",
               "Firozabad", "Gautam Buddha Nagar", "Ghaziabad", "Ghazipur", "Gonda", "Gorakhpur", "Hamirpur",
               "Hapur (Panchsheel Nagar)", "Hardoi", "Hathras", "Jalaun", "Jaunpur", "Jhansi", "Kannauj",
               "Kanpur Dehat", "Kanpur Nagar", "Kanshiram Nagar (Kasganj) ", "Kaushambi", "Kushinagar (Padrauna)",
               "Lakhimpur - Kheri", "Lalitpur", "Lucknow", "Maharajganj", "Mahoba", "Mainpuri", "Mathura", "Mau",
               "Meerut", "Mirzapur", "Moradabad", "Muzaffarnagar", "Pilibhit", "Pratapgarh", "RaeBareli", "Rampur",
               "Saharanpur", "Sambhal (Bhim Nagar)", "Sant Kabir Nagar", "Shahjahanpur", "Shamali (Prabuddh Nagar)",
               "Shravasti", "Siddharth Nagar", "Sitapur", "Sonbhadra", "Sultanpur", "Unnao", "Varanasi"]
district_28 = ["Almora", "Bageshwar", "Chamoli", "Champawat", "Dehradun", "Haridwar", "Nainital", "Pauri Garhwal",
               "Pithoragarh", "Rudraprayag", "Tehri Garhwal", "Udham Singh Nagar", "Uttarkashi"]
district_29 = ["Alipurduar", "Bankura", "Birbhum", "Cooch Behar", "Dakshin Dinajpur (South Dinajpur)", "Darjeeling",
               "Hooghly", "Howrah", "Jalpaiguri", "Jhargram", "Kalimpong", "Kolkata", "Malda", "Murshidabad", "Nadia",
               "North 24 Parganas", "Paschim Medinipur (West Medinipur)", "Paschim (West) Burdwan (Bardhaman)",
               "Purba Burdwan (Bardhaman)", "Purba Medinipur (East Medinipur)", "Purulia", "South 24 Parganas",
               "Uttar Dinajpur (North Dinajpur)"]
district_30 = ["Nicobar", "North and Middle Andaman", "South Andaman"]
district_31 = ["Chandigarh"]
district_32 = ["Dadra & Nagar Haveli"]
district_33 = ["Daman and Diu"]
district_34 = ["Lakshadweep"]
district_35 = ["Central Delhi", "East Delhi", "New Delhi", "North Delhi", "North East Delhi", "North West Delhi",
               "Shahdara", "South Delhi", "South East Delhi", "South West Delhi", "West Delhi"]
district_36 = ["Karaikal", "Mahe", "Puducherry", "Yanam"]
district = [district_1, district_2, district_3, district_4, district_5, district_6, district_7, district_8, district_9,
            district_10, district_11, district_12, district_13, district_14, district_15, district_16, district_17,
            district_18, district_19, district_20, district_21, district_22, district_23, district_24, district_25,
            district_26, district_27, district_28, district_29, district_30, district_31, district_32, district_33,
            district_34, district_35, district_36]


def random_states():
    global states
    a = random.randint(0, len(states) - 1)
    return states[a]


def random_districts(states_name):
    global states, district
    a = states.index(states_name)
    district_name = district[a]
    b = random.randint(0, len(district_name) - 1)
    return district_name[b]
