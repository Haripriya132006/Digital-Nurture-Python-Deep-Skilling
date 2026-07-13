import  {courses} from "./data.js";
import renderCourses from "./app.js";
import {courseGrid} from "./app.js";

function fetchUserPromise(id){
return fetch('https://jsonplaceholder.typicode.com/users/'+id)
.then(response=>{
          if(!response.ok){
          throw new Error('Network response was not ok');
          }
          return response.json();
})
.then(user=>{
          console.log('User Name (Promise):',user.name,id)
})
.catch(error =>{
          console.error('Error fetching user:',error);
});
}
fetchUserPromise(5);

async function fetchUserAsync(id){
try{
          const response=await fetch('https://jsonplaceholder.typicode.com/users/'+id);
          if(!response.ok){
          throw new Error('Network response was not ok');
          }
          const user=await response.json();
          console.log('User Name (Async/Await):',user.name);
          return user;
}
catch(error){
          console.error('Error fetching user inside async:',error);
}
}
fetchUserAsync(4);

const localCourses=[
{id:6,name:'JavaScript Basics'},
{id:7,name:'MERN full stack'},
{id:8,name:'UI design'}
]

function fetchAllCourses(){
return new Promise(resolve => {
          setTimeout(() => {
          const combined=[...localCourses,...courses]
          resolve(combined);
          }, 1000);
});
}

function loadAndDisplayCourses() {
// 1. Show the loading message in the UI right away
          courseGrid.innerHTML = '<p class="loading-message">Loading courses...</p>';

          // 2. Call the simulated network request
          fetchAllCourses()
                    .then(data => {
                              renderCourses(data);
                    })
                    .catch(error => {
                              courseGrid.innerHTML = '<p class="error-message">Error loading data.</p>';
                              console.error(error);
                    });
}

loadAndDisplayCourses();


async function fetchTwoUsersSimultaneously() {
          const url1 = 'https://jsonplaceholder.typicode.com/users/1';
          const url2 = 'https://jsonplaceholder.typicode.com/users/2';

          try {
          // 1. Kick off both fetch requests at the exact same time
          const [response1, response2] = await Promise.all([
                    fetch(url1),
                    fetch(url2)
          ]);

          if (!response1.ok || !response2.ok) {
                    throw new Error('One or both network responses failed');
          }

          const [user1, user2] = await Promise.all([
                    response1.json(),
                    response2.json()
          ]);

          console.log(`Promise.all Results -> User 1: ${user1.name} | User 2: ${user2.name}`);

          } catch (error) {
                    console.error('Error during simultaneous fetching:', error);
          }
}

// Execute the function
fetchTwoUsersSimultaneously();