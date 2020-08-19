from tensorforce.agents import Agent
from tensorforce.environments import Environment
from tensorforce.execution import Runner

from bad_seeds.simple.bad_seeds_01 import BadSeeds01


def main():

    bad_seeds_environment = Environment.create(
        environment=BadSeeds01, max_episode_timesteps=100,
    )

    agent = Agent.create(
        agent="a2c",
        batch_size=100,  # this seems to help a2c
        horizon=20,  # does this help a2c?
        exploration=0.01,  # tried without this at first
        l2_regularization=0.1,
        entropy_regularization=0.2,
        variable_noise=0.05,
        environment=bad_seeds_environment,
        summarizer=dict(
            directory="training_data/agent_01_env_01/summaries",
            # list of labels, or 'all'
            labels=["graph", "entropy", "kl-divergence", "losses", "rewards"],
            frequency=100,  # store values every 100 timesteps
        ),
    )

    runner = Runner(agent=agent, environment=bad_seeds_environment)
    runner.run(num_episodes=10)
    agent.save(directory="saved_models")


if __name__ == "__main__":
    main()
