"""
Utilities for handling phase picks in SeisBench-compatible format.

This module provides functions to create, validate, and convert phase picks
to a standardized CSV format compatible with both SeisBench and PyOcto.
"""

import pandas as pd
from typing import List, Optional
from datetime import datetime


def create_picks_dataframe(
    station_ids: List[str],
    phase_times: List[datetime],
    phase_labels: List[str],
    phase_scores: Optional[List[float]] = None,
    phase_indexes: Optional[List[int]] = None,
    **kwargs
) -> pd.DataFrame:
    """
    Create a standardized picks DataFrame in SeisBench format.
    
    Parameters
    ----------
    station_ids : list of str
        Station identifiers (e.g., "NET.STA.LOC.CHA")
    phase_times : list of datetime
        Phase arrival times
    phase_labels : list of str
        Phase type labels ("P", "S", etc.)
    phase_scores : list of float, optional
        Confidence scores for picks (0-1)
    phase_indexes : list of int, optional
        Sample indices in the original trace
    **kwargs : dict
        Additional metadata columns (e.g., event_id, trace_name, latitude, longitude)
    
    Returns
    -------
    pd.DataFrame
        SeisBench-compatible picks DataFrame with columns:
        - station_id: Station identifier
        - phase_time: Phase arrival time (datetime)
        - phase_label: Phase type (P, S, etc.)
        - phase_score: Pick confidence (0-1)
        - phase_index: Sample index in trace
        - Additional metadata columns from kwargs
    """
    data = {
        'station_id': station_ids,
        'phase_time': phase_times,
        'phase_label': phase_labels,
    }
    
    if phase_scores is not None:
        data['phase_score'] = phase_scores
    else:
        data['phase_score'] = [1.0] * len(station_ids)
    
    if phase_indexes is not None:
        data['phase_index'] = phase_indexes
    
    # Add any additional metadata columns
    for key, value in kwargs.items():
        data[key] = value
    
    return pd.DataFrame(data)


def save_picks_csv(picks_df: pd.DataFrame, output_path: str) -> None:
    """
    Save picks DataFrame to CSV in standardized format.
    
    Parameters
    ----------
    picks_df : pd.DataFrame
        DataFrame containing phase picks
    output_path : str
        Path to output CSV file
    """
    picks_df.to_csv(output_path, index=False)
    print(f"Saved {len(picks_df)} picks to {output_path}")


def load_picks_csv(csv_path: str) -> pd.DataFrame:
    """
    Load picks from standardized CSV format.
    
    Parameters
    ----------
    csv_path : str
        Path to input CSV file
    
    Returns
    -------
    pd.DataFrame
        Picks DataFrame with phase_time parsed as datetime
    """
    picks_df = pd.read_csv(csv_path, parse_dates=['phase_time'])
    return picks_df


def filter_picks_by_phase(picks_df: pd.DataFrame, phase_label: str) -> pd.DataFrame:
    """
    Filter picks by phase type.
    
    Parameters
    ----------
    picks_df : pd.DataFrame
        Picks DataFrame
    phase_label : str
        Phase type to filter (e.g., "P", "S")
    
    Returns
    -------
    pd.DataFrame
        Filtered picks DataFrame
    """
    return picks_df[picks_df['phase_label'] == phase_label].copy()


def merge_picks(picks_list: List[pd.DataFrame], remove_duplicates: bool = True) -> pd.DataFrame:
    """
    Merge multiple picks DataFrames.
    
    Parameters
    ----------
    picks_list : list of pd.DataFrame
        List of picks DataFrames to merge
    remove_duplicates : bool, optional
        If True, remove duplicate picks based on station_id, phase_time, and phase_label
    
    Returns
    -------
    pd.DataFrame
        Merged picks DataFrame
    """
    merged = pd.concat(picks_list, ignore_index=True)
    
    if remove_duplicates:
        merged = merged.drop_duplicates(
            subset=['station_id', 'phase_time', 'phase_label'],
            keep='first'
        )
    
    return merged


def validate_picks_schema(picks_df: pd.DataFrame) -> bool:
    """
    Validate that picks DataFrame has required columns.
    
    Parameters
    ----------
    picks_df : pd.DataFrame
        Picks DataFrame to validate
    
    Returns
    -------
    bool
        True if schema is valid
    
    Raises
    ------
    ValueError
        If required columns are missing
    """
    required_columns = ['station_id', 'phase_time', 'phase_label', 'phase_score']
    missing_columns = [col for col in required_columns if col not in picks_df.columns]
    
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")
    
    return True
