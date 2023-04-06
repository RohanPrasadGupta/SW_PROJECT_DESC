import { Component, OnInit } from '@angular/core';
import { ApiService } from '../ApiService';
import { Overtime } from '../worker';

@Component({
  selector: 'app-overtime',
  templateUrl: './overtime.component.html',
  styleUrls: ['./overtime.component.css']
})
export class OvertimeComponent {

  overtimes: Overtime[] = [];
  constructor(private apiService: ApiService) { }

  ngOnInit(): void {
    this.getOvertimes();
  }

  getOvertimes() {
    this.apiService.getOverTime().subscribe(
      (response: any) => {
        this.overtimes = response;
      },
      (error: any) => {
        console.log(error);
      }
    );
  }
}
