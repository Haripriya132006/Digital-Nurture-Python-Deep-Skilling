async function apifetch(url){
          const response=await fetch(url);
          if(!response.ok){
                    throw new Error(`HTTP Error! Status: ${response.status}`);
          }
          return await response.json();
}

const notificationsSection=document.getElementById('notifications');
let currentFetchUrl='https://jsonplaceholder.typicode.com/posts';

async function loadNotifications(url){
          currentFetchUrl=url;

          notificationsSection.innerHTML=`
          <div class="loading-container">
                    <p class="loading-text">Loading notifications...</p>
                    <div class="spinner"></div>
          </div>
          `;

          try{
                    await new Promise(resolve=>setTimeout(resolve,2000)); //this delays and leads to load notificationsqs
                    const posts=await apifetch(url);
                    const displayPosts=posts.slice(0,5);

                    notificationsSection.innerHTML='';
                    displayPosts.forEach(post=>{
                              const card=document.createElement('div');
                              card.className='notification-card';
                              card.innerHTML=`
                              <h4>${post.title}</h4>
                              <p>${post.body}</p>
                              `
                              notificationsSection.appendChild(card);
                    });
          }
          catch(error){
                    notificationsSection.innerHTML=`
                    <div class="error-container">
                              <p class="error-message">Failed to load notifications</p>
                              <p>${error.message}</p>
                              <button id="retry" class="retry-btn">Retry </button>
                    </div>
                    `
                    document.getElementById('retry').addEventListener('click',()=>{
                              console.log('Retrying fetch for:',currentFetchUrl);
                              loadNotifications(currentFetchUrl);
                    });
          }
}

// loadNotifications('https://jsonplaceholder.typicode.com/nonexistant')