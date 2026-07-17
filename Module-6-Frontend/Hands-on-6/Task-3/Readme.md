```
import {createSlice} from '@reduxjs/toolkit';

const initialState={
          enrolledCourses:[]
};

const enrollmentSlice=createSlice({
          name:'enrollment',
          initialState,
          reducers:{
                    enroll:(state,action)=>{
                              const courseExists=state.enrolledCourses.some(c=>c.id===action.payload.id);
                              if (!courseExists){
                                        state.enrolledCourses.push(action.payload);
                              }
                    },
                    unenroll:(state,action)=>{
                              state.enrolledCourses=state.enrolledCourses.filter(c=>c.id!==action.payload);
                    }
          }
});

export const {enroll,unenroll}=enrollmentSlice.actions;

export default enrollmentSlice.reducer;
```


```
import { configureStore } from '@reduxjs/toolkit';
import enrollmentReducer from './enrollmentSlice';

export const store = configureStore({
  reducer: {
    enrollment: enrollmentReducer
  }
});
```

```
import {useSelector,useDispatch} from 'react-redux';
import {unenroll} from '../store/enrollmentSlice';

```

```
 const dispatch=useDispatch();
  const enrolledCourses=useSelector((state)=>state.enrollment.enrolledCourses);
```


```
              <button onClick={() => dispatch(unenroll(course.id))} style={{ marginLeft: '10px', color: 'red' }}>Un-enroll</button>

```

![alt text](<Screenshot 2026-07-17 133411.png>)