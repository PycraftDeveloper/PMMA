
void PMMA::FastRandom::SetSeed() {
    std::random_device rd;
    uint64_t rd_seed = (static_cast<uint64_t>(rd()) << 32) | rd();

    // Get current system time in nanoseconds
    uint64_t time_seed = std::chrono::high_resolution_clock::now().time_since_epoch().count();

    // Combine both: if rd() fails and returns a constant, time_seed still ensures uniqueness
    uint64_t seed = rd_seed ^ time_seed;

    s[0] = splitmix64(seed);
    s[1] = splitmix64(seed);
}