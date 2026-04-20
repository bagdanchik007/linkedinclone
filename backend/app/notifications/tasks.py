import asyncio
from app.core.database import async_session_maker
from app.notifications.service import create_notification


async def _notify_connection_request(receiver_id: str, requester_id: str, requester_email: str):
    async with async_session_maker() as db:
        await create_notification(
            db=db,
            user_id=receiver_id,
            type="connection_request",
            payload={
                "requester_id": requester_id,
                "requester_email": requester_email,
            },
        )


async def _notify_application_update(applicant_id: str, job_title: str, new_status: str):
    async with async_session_maker() as db:
        await create_notification(
            db=db,
            user_id=applicant_id,
            type="application_update",
            payload={
                "job_title": job_title,
                "new_status": new_status,
            },
        )


async def _notify_new_job(user_id: str, job_id: str, job_title: str, company: str):
    async with async_session_maker() as db:
        await create_notification(
            db=db,
            user_id=user_id,
            type="new_job",
            payload={
                "job_id": job_id,
                "job_title": job_title,
                "company": company,
            },
        )