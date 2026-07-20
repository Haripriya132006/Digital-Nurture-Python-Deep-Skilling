import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import {FormsModule} from '@angular/forms';
import { CourseCard } from '../course-card/course-card';
import { CourseService } from '../course';

// interfaces should not come in betweeen component and its class
interface Course{
  name:string;
  code:string;
  credits:number;
  grade:string;
}


@Component({
  selector: 'app-course-list',
  imports: [CommonModule,FormsModule,CourseCard],
  templateUrl: './course-list.html',
  styleUrl: './course-list.css',
})



export class CourseList implements OnInit {
  searchTerm:string='';
  courses:any[]=[];
  loading:boolean=true;
  // courses:Course[]=[
  //   {name:'Angular',code:'CS101',credits:4,grade:'A'},
  //   {name:'Python',code:'IT101',credits:3,grade:'B'},
  //   {name:'Prompt Engineering',code:'AI101',credits:2,grade:'A'},
  //   {name:'Design Engineering',code:'ME101',credits:3,grade:'B'},
  //   {name:'HRM',code:'HS101',credits:3,grade:'A'},
  // ];
  constructor(private courseService:CourseService){}

  ngOnInit():void{
    this.loading=true;
    this.courseService.getCourses().subscribe({
      next:(data)=>{
        this.courses=data.map((item:any)=>({
          name:item.title,
          code:`CS${item.id}`,
          credits:(item.id%2==0)?4:3,
          grade:(item.id%2==0)?'B':'A'
        }));
        this.loading=false;
      },
      error:(err)=>{
        console.error('Failed to load courses',err);
        this.loading=false;
      }
    });
  }

  get filteredCourses():Course[]{
    return this.courses.filter(course=>
      course.name.toLowerCase().includes(this.searchTerm.toLowerCase())
    );
  }
}
