export interface Worker {
    id: string;
    name: string;
    device_id: string;
    phone: number;
    lat: number;
    lon: number;
    emergency: number;
    emergency_id: number;
    on_site: boolean;
    last_updated: string;
  }

export interface Emergency{
  worker_id: string;
  lat: number;
  lon: number;
  on_site: boolean;
  case_type: null;
  case_status: false;
  note:"resolved"; 
}

export interface Overtime{
  worker_id: string;
  name: string;
  date: string;
  check_in: string;
  check_out: string;
  overtime: number;
}
  