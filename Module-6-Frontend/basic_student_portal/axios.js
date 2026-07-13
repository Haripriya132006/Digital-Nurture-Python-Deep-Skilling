import {courses} from "./data.js";

axios.interceptors.request.use((config)=>{
          console.log(`api call started: ${config.url}`);
          return config;
},
(error)=>{
          return Promise.reject(error);
});

async function apiFetchAxios(url){
          const response=await axios.get(url);
          return response.data;
}

async function fetchUserOnePosts(){
          const targetUrl='https://jsonplaceholder.typicode.com/posts';
          try{
                    const response=await axios.get(targetUrl,{
                              params:{userId:1}
                    });
                    console.log('user 1 posts fetched',response.data);
          }
          catch(error){
                    console.log('error feching user posts',error.message);
          }
}

fetchUserOnePosts();
apiFetchAxios('https://jsonplaceholder.typicode.com/nonexistent')
          .catch(err=> console.log('axios caugth this 404 error',err.message));