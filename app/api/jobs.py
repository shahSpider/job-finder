from app.main import app

@app.get("/jobs")
def get_jobs():
    return {"jobs": ["job1", "job2", "job3"]}

@app.post("/jobs")
def create_job(job: str):
    return {"message": f"Job '{job}' created successfully"}

@app.delete("/jobs/{job_id}")
def delete_job(job_id: int):
    return {"message": f"Job with ID {job_id} deleted successfully"}

@app.put("/jobs/{job_id}")
def update_job(job_id: int, job: str):
    return {"message": f"Job with ID {job_id} updated to '{job}' successfully"}
