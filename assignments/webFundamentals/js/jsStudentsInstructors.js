
var students = [
  {first_name:  'Michael', last_name : 'Jordan'},
  {first_name : 'John', last_name : 'Rosales'},
  {first_name : 'Mark', last_name : 'Guillen'},
  {first_name : 'KB', last_name : 'Tonel'}
]

var users = {
 'Students': [
     {first_name:  'Michael', last_name : 'Jordan'},
     {first_name : 'John', last_name : 'Rosales'},
     {first_name : 'Mark', last_name : 'Guillen'},
     {first_name : 'KB', last_name : 'Tonel'}
  ],
 'Instructors': [
     {first_name : 'Michael', last_name : 'Choi'},
     {first_name : 'Martin', last_name : 'Puryear'}
  ]
 }

 function justStudents(studentsObject){
   for(var item in studentsObject){
     console.log(studentsObject[item].first_name, studentsObject[item].last_name);
   }
 }

justStudents(students)

console.log('---------------------------');

function studsAndTeachers(sNt){
  for(var key in sNt){
    var counter = 1
    var idx = 0;
    console.log(key);
    while(idx < sNt[key].length){
      var num = Math.floor(Math.random()*15);
      console.log(counter,'-', sNt[key][idx].first_name, sNt[key][idx].last_name,'-', num );
      idx ++;
      counter ++;
    }
  }
}

studsAndTeachers(users)
console.log('---------------------------');
