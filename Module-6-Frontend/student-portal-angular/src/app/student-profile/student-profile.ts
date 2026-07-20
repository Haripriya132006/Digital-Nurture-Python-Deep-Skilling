import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { FormControl, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';

@Component({
  selector: 'app-student-profile',
  imports: [CommonModule,ReactiveFormsModule],
  templateUrl: './student-profile.html',
  styleUrl: './student-profile.css',
})
export class StudentProfile {
  profileForm=new FormGroup({
    name:new FormControl('',[Validators.required]),
    email:new FormControl('',[Validators.required,Validators.email]),
    semester:new FormControl('',[Validators.required,Validators.min(1),Validators.max(8)])
  });

  onSubmit():void{
    if(this.profileForm.valid){
      alert('Form Submitted');
      console.log('Form submitted: ',this.profileForm.value);
    }
  }
}
