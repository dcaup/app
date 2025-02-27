# -*- coding: utf-8 -*-
"""io.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17kT79QBW6M6BQtdHo6oeEaW7dHAhQaUU
"""

# -*- coding: utf-8 -*-
"""Unified Pipeline for Financial Decision-Making with crossmodal, Decentralized Agents

This notebook simulates a system of multiple, decentralized agents that
process crossmodal data (numerical financial data, news text, and social media
sentiment) to make financial decisions (e.g., buy/sell/hold recommendations).
It focuses on demonstrating the data flow, analysis, and explainability
aspects of such a system.

Workflow:
1. Data Generation (Synthetic): Create synthetic data for:
    - Financial time series (e.g., stock prices).
    - News headlines (text).
    - Social media sentiment scores.
2. Agent Simulation: Simulate multiple agents with different strategies.
3. Data Processing: Each agent processes the data relevant to its strategy.
4. Decision Making: Each agent makes a decision (buy/sell/hold).
5. Aggregation (Simplified): Combine agent decisions (e.g., majority voting).
6. Visualization: Visualize the data and agent decisions with various plots.
7. Statistical Summary: Generate summary statistics and perform bootstrap analysis.
8. LLM Insights Report: Synthesize findings using simulated LLMs.

Keywords: crossmodal Data, Decentralized Agents, Financial Decision-Making, Simulation, Explainability, LLMs, Data Visualization, Time Series, Bootstrap
"""

!pip install pandas matplotlib seaborn plotly scipy
import warnings
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import numpy as np
from io import StringIO
import plotly.express as px
from scipy.stats import bootstrap, gaussian_kde

# Suppress warnings (use with caution in production)
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=UserWarning, module="plotly")

# Google Colab environment check
try:
    from google.colab import drive
    drive.mount("/content/drive")
    COLAB_ENV = True
except ImportError:
    COLAB_ENV = False
    print("Not running in Google Colab environment.")

# Constants
OUTPUT_PATH = "./output_crossmodal_agents/" if not COLAB_ENV else "/content/drive/MyDrive/output_crossmodal_agents/"
NUM_AGENTS = 3  # Number of simulated agents
NUM_DAYS = 100  # Number of days of simulated data
MODEL_GROK_NAME = "grok-base"
MODEL_CLAUDE_NAME = "claude-3.7-sonnet"
MODEL_GROK_ENHANCED_NAME = "grok-enhanced"
LINE_WIDTH = 2.5
BOOTSTRAP_RESAMPLES = 500

# Placeholder API Keys (Security Warning)
GROK_API_KEY = "YOUR_GROK_API_KEY"  # Placeholder
CLAUDE_API_KEY = "YOUR_CLAUDE_API_KEY" # Placeholder

# --- Helper Functions ---

def create_output_directory(path):
    """Creates the output directory if it doesn't exist, handling errors."""
    try:
        os.makedirs(path, exist_ok=True)
        return True
    except OSError as e:
        print(f"Error creating output directory: {e}")
        return False

def analyze_text_with_llm(text, model_name):
    """Placeholder for LLM analysis.  Replace with actual API calls."""
    text_lower = text.lower()
    if model_name == MODEL_GROK_NAME:
        if "crossmodal" in text_lower: return "Grok-base: Analysis considers multiple data sources."
        elif "decentralized" in text_lower: return "Grok-base: Decentralized agents contribute to the decision."
        else: return f"Grok-base: General analysis on '{text}'."
    elif model_name == MODEL_CLAUDE_NAME:
        if "financial decision" in text_lower: return "Claude 3.7: Analysis focuses on the financial decision-making process."
        elif "agent" in text_lower: return "Claude 3.7: Agent behavior and decision-making are analyzed."
        else: return f"Claude 3.7: Enhanced analysis on '{text}'."
    elif model_name == MODEL_GROK_ENHANCED_NAME:
        if "crossmodal" in text_lower and "decentralized" in text_lower: return "Grok-Enhanced: The crossmodal, decentralized approach provides a more robust and comprehensive analysis for financial decision-making."
        elif "agent" in text_lower: return "Grok-Enhanced: Analysis reveals how individual agents process information and interact to reach a collective decision."
        else: return f"Grok-Enhanced: In-depth analysis on '{text}'."
    return f"Model '{model_name}' not supported."

# --- Data Generation (Synthetic) ---

def generate_synthetic_financial_data(num_days=NUM_DAYS):
    """Generates synthetic financial time series data."""
    np.random.seed(42)  # For reproducibility
    dates = pd.date_range("2024-01-01", periods=num_days, freq="D")
    prices = 100 + np.cumsum(np.random.randn(num_days))  # Random walk
    volume = 1000 + 500 * np.random.rand(num_days)  # Random volume
    return pd.DataFrame({'date': dates, 'price': prices, 'volume': volume})

def generate_synthetic_news_data(num_days=NUM_DAYS):
    """Generates synthetic news headlines (text data)."""
    headlines = [
        "Market Surges Amid Positive Economic News",
        "Tech Stocks Lead the Way in Bull Market",
        "Concerns Grow Over Rising Inflation",
        "Central Bank Announces Interest Rate Hike",
        "New Regulations Impact Financial Sector",
        "Global Trade Tensions Escalate",
        "Company X Reports Record Profits",
        "Economic Slowdown Predicted for Next Quarter",
        "Investors React to Geopolitical Uncertainty",
        "Cryptocurrency Market Experiences Volatility",
    ]
    # Randomly sample headlines for each day
    return pd.DataFrame({'date': pd.date_range("2024-01-01", periods=num_days, freq="D"),
                         'headline': np.random.choice(headlines, num_days)})

def generate_synthetic_sentiment_data(num_days=NUM_DAYS):
    """Generates synthetic sentiment scores (-1 to 1)."""
    return pd.DataFrame({'date': pd.date_range("2024-01-01", periods=num_days, freq="D"),
                         'sentiment': np.random.uniform(-1, 1, num_days)})

# --- Agent Simulation ---

def agent_decision(financial_data, news_data, sentiment_data, agent_type):
    """Simulates an agent's decision based on its strategy."""
    # Placeholder logic - Replace with more sophisticated strategies
    last_price = financial_data['price'].iloc[-1]
    sentiment = sentiment_data['sentiment'].iloc[-1]

    if agent_type == "technical":  # Simple moving average strategy
        if last_price > financial_data['price'].tail(5).mean():  # Above 5-day MA
            return "buy"
        else:
            return "sell"
    elif agent_type == "sentiment":  # Sentiment-based strategy
        if sentiment > 0.5:
            return "buy"
        elif sentiment < -0.5:
            return "sell"
        else:
            return "hold"
    elif agent_type == "fundamental": # Placeholder - would need more data
        # Simulate based on news keywords (very simplified)
        last_headline = news_data['headline'].iloc[-1]
        if "Positive" in last_headline or "Profits" in last_headline:
            return "buy"
        elif "Concerns" in last_headline or "Slowdown" in last_headline:
            return "sell"
        else:
            return "hold"
    else:
        return "hold"  # Default action

# --- Data Processing and Decision Making ---

def process_data_and_make_decisions(financial_data, news_data, sentiment_data, num_agents=NUM_AGENTS):
    """Simulates data processing and decision-making by multiple agents."""
    agent_types = ["technical", "sentiment", "fundamental"]
    decisions = {}
    for i in range(num_agents):
        agent_type = agent_types[i % len(agent_types)]  # Cycle through agent types
        decision = agent_decision(financial_data, news_data, sentiment_data, agent_type)
        decisions[f"agent_{i+1}"] = (agent_type, decision)
    return decisions

def aggregate_decisions(decisions):
    """Aggregates agent decisions (simplified - majority voting)."""
    # Count the occurrences of each decision
    decision_counts = {}
    for agent, (agent_type, decision) in decisions.items():
        if decision not in decision_counts:
            decision_counts[decision] = 0
        decision_counts[decision] += 1

    # Find the most frequent decision
    majority_decision = max(decision_counts, key=decision_counts.get)
    return majority_decision

# --- Visualization ---
def create_combined_plot(financial_data, news_data, sentiment_data, decisions, output_path):
    """Creates a combined plot showing price, sentiment, and agent decisions."""
    try:
        fig, ax1 = plt.subplots(figsize=(14, 8))
        plt.style.use('dark_background')

        # Price data
        ax1.plot(financial_data['date'], financial_data['price'], color="#00FFFF", label='Price', linewidth=LINE_WIDTH)
        ax1.set_xlabel('Date', color='white')
        ax1.set_ylabel('Price', color="#00FFFF")
        ax1.tick_params(axis='y', labelcolor="#00FFFF")

        # Sentiment data (secondary y-axis)
        ax2 = ax1.twinx()
        ax2.plot(sentiment_data['date'], sentiment_data['sentiment'], color="#FF00FF", label='Sentiment', linewidth=LINE_WIDTH)
        ax2.set_ylabel('Sentiment', color="#FF00FF")
        ax2.tick_params(axis='y', labelcolor="#FF00FF")
        ax2.set_ylim(-1, 1)  # Sentiment is between -1 and 1

        # Agent decisions (vertical lines)
        for agent, (agent_type, decision) in decisions.items():
            if decision == "buy":
                color = 'green'
            elif decision == "sell":
                color = 'red'
            else:  # hold
                color = 'gray'
            # Use the last date for simplicity (in a real system, you'd have decision timestamps)
            ax1.axvline(financial_data['date'].iloc[-1], color=color, linestyle='--', alpha=0.7, label=f"{agent} ({agent_type}): {decision}")

        plt.title('Combined Financial Data, Sentiment, and Agent Decisions', color='white')
        fig.tight_layout()
        plt.legend(facecolor='black', edgecolor='white', labelcolor='white')
        plt.savefig(os.path.join(output_path, "combined_plot.png"))
        plt.close()
        return "Combined plot generated successfully."

    except Exception as e:
        print(f"Error creating combined plot: {e}")
        return "Error creating combined plot."

def create_distribution_plots(financial_data, output_path):
    """Creates distribution plots (histogram, KDE, violin) for price and volume."""
    try:
        # Price Distribution
        fig, axes = plt.subplots(1, 3, figsize=(18, 6))
        plt.style.use('dark_background')

        # Histogram
        sns.histplot(financial_data['price'], kde=False, bins=30, ax=axes[0], color="#00FFFF")
        axes[0].set_title('Price Histogram', color='white')

        # KDE Plot
        sns.kdeplot(financial_data['price'], ax=axes[1], color="#00FFFF", linewidth=LINE_WIDTH)
        axes[1].set_title('Price KDE', color='white')

        # Violin Plot
        sns.violinplot(y=financial_data['price'], ax=axes[2], color="#00FFFF")
        axes[2].set_title('Price Violin Plot', color='white')

        plt.tight_layout()
        plt.savefig(os.path.join(output_path, "price_distribution.png"))
        plt.close()


        # Volume Distribution
        fig, axes = plt.subplots(1, 3, figsize=(18, 6))

        # Histogram
        sns.histplot(financial_data['volume'], kde=False, bins=30, ax=axes[0], color="#FF00FF")
        axes[0].set_title('Volume Histogram', color='white')

        # KDE Plot
        sns.kdeplot(financial_data['volume'], ax=axes[1], color="#FF00FF", linewidth=LINE_WIDTH)
        axes[1].set_title('Volume KDE', color='white')

        # Violin Plot
        sns.violinplot(y=financial_data['volume'], ax=axes[2], color="#FF00FF")
        axes[2].set_title('Volume Violin Plot', color='white')

        plt.tight_layout()
        plt.savefig(os.path.join(output_path, "volume_distribution.png"))
        plt.close()

        return "Distribution plots generated successfully."

    except Exception as e:
        print(f"Error creating distribution plots: {e}")
        return "Error creating distribution plots."

def create_interactive_plot(financial_data, output_path):
    """Creates an interactive time series plot using Plotly."""
    try:
        fig = px.line(financial_data, x='date', y='price', title='Interactive Price Chart')
        fig.update_layout(
            plot_bgcolor='black',
            paper_bgcolor='black',
            font_color='white'
        )
        fig.write_html(os.path.join(output_path, "interactive_price_chart.html"))
        return "Interactive plot generated successfully."
    except Exception as e:
        print(f"Error creating interactive plot: {e}")
        return "Error creating interactive plot."

def create_correlation_heatmap(financial_data, sentiment_data, output_path):
    """Creates a correlation heatmap of price, volume, and sentiment."""
    try:
        # Combine data for correlation analysis
        combined_data = pd.merge(financial_data, sentiment_data, on='date')
        correlation_matrix = combined_data[['price', 'volume', 'sentiment']].corr()

        plt.figure(figsize=(8, 6))
        sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
        plt.title('Correlation Heatmap (Price, Volume, Sentiment)', color='white')
        plt.savefig(os.path.join(output_path, "correlation_heatmap.png"))
        plt.close()
        return "Correlation heatmap generated successfully."

    except Exception as e:
        print(f"Error creating correlation heatmap: {e}")
        return "Error creating correlation heatmap."

# --- Statistical Summary and Insights ---

def generate_summary_statistics(financial_data):
    """Generates summary statistics for the financial data."""
    return financial_data.describe().to_string()

def perform_bootstrap(data, statistic, n_resamples=BOOTSTRAP_RESAMPLES):
    """Performs bootstrap analysis, handling errors."""
    try:
        bootstrap_result = bootstrap((data,), statistic, n_resamples=n_resamples, method='percentile', random_state=42) # Added random_state
        return bootstrap_result.confidence_interval
    except Exception as e:
        print(f"Error during bootstrap analysis: {e}")
        return (None, None)

def generate_insights_report(summary_stats_text, decisions, output_path):
    """Generates an insights report using (simulated) LLM calls."""

    # Format agent decisions for the report
    decisions_text = "\n".join(
        [f"  - {agent}: {decision_type} -> {decision}" for agent, (decision_type, decision) in decisions.items()]
    )
    aggregated_decision = aggregate_decisions(decisions)

    grok_insights = analyze_text_with_llm(f"Analyze summary statistics:\n{summary_stats_text}\n\nAgent Decisions:\n{decisions_text}", MODEL_GROK_NAME)
    claude_insights = analyze_text_with_llm(f"Analyze agent decisions:\n{decisions_text}", MODEL_CLAUDE_NAME)
    grok_enhanced_insights = analyze_text_with_llm(f"Synthesize findings and provide overall recommendations based on the crossmodal data and agent decisions. Aggregated Decision: {aggregated_decision}", MODEL_GROK_ENHANCED_NAME)

    combined_insights = f"""
Combined Insights Report: crossmodal Financial Decision-Making

Grok-base Analysis:
{grok_insights}

Claude 3.7 Sonnet Analysis:
{claude_insights}

Grok-Enhanced Analysis:
{grok_enhanced_insights}

Synthesized Summary:
This report summarizes the simulated financial data and the decisions made by the decentralized agents. Grok-base provides a general overview of the data and agent decisions. Claude 3.7 focuses on the agent behavior and decision-making process. Grok-Enhanced synthesizes the findings and offers a more in-depth analysis, considering the crossmodal nature of the data and the decentralized agent approach. The aggregated decision of the agents is: {aggregated_decision}.  Further analysis would involve backtesting these decisions against a held-out dataset.
"""
    try:
        with open(os.path.join(output_path, 'insights.txt'), 'w') as f:
            f.write(combined_insights)
        print(f"Insights saved to: {os.path.join(output_path, 'insights.txt')}")
        return "Insights report generated successfully."
    except Exception as e:
        print(f"Error generating insights report: {e}")
        return "Error generating insights report."

# --- Main Script ---

def main():
    """Main function to execute the analysis pipeline."""
    if not create_output_directory(OUTPUT_PATH):
        exit()

    # 1. Data Generation
    financial_data = generate_synthetic_financial_data()
    news_data = generate_synthetic_news_data()
    sentiment_data = generate_synthetic_sentiment_data()

    # 2. Agent Simulation and Decision Making
    decisions = process_data_and_make_decisions(financial_data, news_data, sentiment_data)

    # 3. Visualization
    plot_description = create_combined_plot(financial_data, news_data, sentiment_data, decisions, OUTPUT_PATH)
    print(plot_description)

    distribution_plot_description = create_distribution_plots(financial_data, OUTPUT_PATH)
    print(distribution_plot_description)

    interactive_plot_description = create_interactive_plot(financial_data, OUTPUT_PATH)
    print(interactive_plot_description)

    correlation_heatmap_description = create_correlation_heatmap(financial_data, sentiment_data, OUTPUT_PATH)
    print(correlation_heatmap_description)


    # 4. Statistical Summary
    summary_stats_text = generate_summary_statistics(financial_data)
    # Example: Bootstrap CI for the mean price (you could do this for other metrics too)
    bootstrap_ci_price = perform_bootstrap(financial_data['price'], np.mean)
    summary_stats_text += f"\nBootstrap CI for mean price: {bootstrap_ci_price}"

    # 5. LLM Insights Report
    generate_insights_report(summary_stats_text, decisions, OUTPUT_PATH)

    print("Execution completed successfully.")

if __name__ == "__main__":
    main()