import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Worker, Emergency } from './worker';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private baseUrl = 'http://zunzun.pythonanywhere.com';
  private token: string = '';

  constructor(private http: HttpClient) { }

  authenticate(username: string, password: string): Observable<any> {
    const credentials = { username: username, password: password };
    return this.http.post(`${this.baseUrl}/api/token/`, credentials);
  }

  setToken(token: string): void {
    this.token = token;
  }

  getToken(): string {
    return this.token;
  }

  getWorkers(): Observable<any> {
    const headers = new HttpHeaders({ 'Authorization': `Bearer ${this.token}` });
    return this.http.get(`${this.baseUrl}/api/workers/`, { headers: headers });
  }

  resolvedEmergency(updatedData: any, id: number){
    const headers = new HttpHeaders({ 'Authorization': `Bearer ${this.token}` });
    return this.http.put(`${this.baseUrl}/api/emergencies/` + id + "/", updatedData, { headers: headers });    
  }

  getOverTime(): Observable<any> {
    const headers = new HttpHeaders({ 'Authorization': `Bearer ${this.token}` });
    return this.http.get(`${this.baseUrl}/api/attendances/overtime/`, { headers: headers });
  }
}
