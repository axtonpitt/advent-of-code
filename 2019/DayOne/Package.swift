// swift-tools-version:5.3

import PackageDescription

let package = Package(
    name: "RocketFuel",
    platforms: [
      .macOS("10.15.4")
    ],
    dependencies: [
        .package(url: "https://github.com/apple/swift-argument-parser", from: "0.3.1"),
    ],
    targets: [
        .target(
            name: "RocketFuel",
            dependencies: [
		.product(name: "ArgumentParser", package: "swift-argument-parser"),
	]),
        .testTarget(
            name: "RocketFuelTests",
            dependencies: ["RocketFuel"]),
    ]
)
