import { Component, Input, OnInit } from '@angular/core';
import { ApiService } from '../ApiService';
import { Worker, Emergency } from '../worker';

@Component({
  selector: 'app-workers',
  templateUrl: './workers.component.html',
  styleUrls: ['./workers.component.css']
})
export class WorkersComponent implements OnInit {
  title = "Workers";
  imageWidth: number = 20;
  imageHeight: number = 52;
  svgWidth: number = 550;
  svgHeight: number = 500;
  recX = 1
  recY = 1
  xMin = this.recX + this.imageWidth / 2;
  xMax = 450
  yMin = this.recY + this.imageHeight / 2;
  yMax = 450
  recWidth: number = this.xMax - this.recX + this.imageWidth;
  recHeight: number = this.yMax - this.recY + this.imageHeight;
  latMin = 14.078292;
  latMax = 14.080311;
  lonMin = 100.602999;
  lonMax = 100.604901;
  radius = 20;
  workers: Worker[] = [];
  colors: String[] = ['darkolivegreen', 'darkorchid', 'darkorange', 'lightseagreen', 'midnightblue', 'black', 'red']

  constructor(private apiService: ApiService) { }

  ngOnInit(): void {
    const callGetWorkers = () => {
      this.getWorkers();
      setTimeout(callGetWorkers, 5000);
    };
    
    callGetWorkers();
  }

  getWorkers() {
    this.apiService.getWorkers().subscribe(
      (response: any) => {
        this.workers = response;
      },
      (error: any) => {
        console.log(error);
      }
    );
  }

  resolvedEmergency(worker: Worker) {
    let temp: number = worker.emergency
    worker.emergency = 0
    let updatedData: any;
    updatedData = {
      "worker_id": worker.id,
      "lat": worker.lat,
      "lon": worker.lon,
      "on_site": worker.on_site,
      "case_type": temp,
      "case_status": true,
      "note": "resolved"
    };
    this.apiService.resolvedEmergency(updatedData, worker.emergency_id).subscribe(response => {
      console.log('Emergency updated successfully:', response);
      // Handle success scenario
    },
      error => {
        console.error('Failed to update emergency:', error);
        // Handle error scenario
      })
  }

  getX(lat: number) {

    return (lat - this.latMin) * (this.xMax - this.xMin) / (this.latMax - this.latMin) + this.xMin
  }

  getY(lon: number) {
    return (lon - this.lonMin) * (this.yMax - this.yMin) / (this.lonMax - this.lonMin) + this.yMin
  }

  getColorIndex(worker: Worker) {
    let idx: number = 0
    if (worker.emergency == 0) {
      idx = parseInt(worker.id.substring(3)) - 1;
    }
    else if (worker.emergency == 1) {
      idx = 5
    } else {
      idx = 6
    }
    return idx;
  }

  getHref(worker: Worker) {
    let link: string = ''
    if (worker.emergency == 0) {
      link = "../assets/images/" + worker.id + ".png";
    } else if (worker.emergency == 1) {
      link = "../assets/images/injury.png";
    } else {
      link = "../assets/images/fire.png";
    }
    return link
  }
}
